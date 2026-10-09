import numpy as np
from sentence_transformers import SentenceTransformer


MODEL_NAME = "intfloat/multilingual-e5-small"

DOCUMENTS = [
    "本文使用李雅普诺夫函数证明系统稳定。",
    "数值实验采用四阶Runge-Kutta方法。",
    "本文研究忆阻神经网络的同步控制。",
    "论文介绍了非线性系统的研究背景。",
]

QUERIES = [
    "论文如何证明系统稳定？",
    "数值实验使用了什么计算方法？",
    "论文研究了什么同步控制问题？",
    "论文的研究背景是什么？",
]

# 每个查询预期最相关的文档下标
EXPECTED_TOP_INDICES = [
    0,
    1,
    2,
    3,
]


def encode_passages(
    model: SentenceTransformer,
    documents: list[str],
    *,
    use_prefix: bool = True,
) -> np.ndarray:
    """将多段候选原文编码成二维向量矩阵。"""
    if not documents:
        raise ValueError("候选文档不能为空")

    if any(not document.strip() for document in documents):
        raise ValueError("候选文档不能包含空文本")

    if use_prefix:
        inputs = [
            f"passage: {document}"
            for document in documents
        ]
    else:
        inputs = documents

    vectors = model.encode(
        inputs,
        batch_size=2,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    if vectors.ndim != 2:
        raise ValueError("Passage编码结果必须是二维矩阵")

    if vectors.shape[0] != len(documents):
        raise ValueError("向量数量与文档数量不一致")

    return vectors


def encode_query(
    model: SentenceTransformer,
    query: str,
    *,
    use_prefix: bool = True,
) -> np.ndarray:
    """将一个查询编码成一维向量。"""
    if not query.strip():
        raise ValueError("查询文本不能为空")

    if use_prefix:
        input_text = f"query: {query}"
    else:
        input_text = query

    # 传入单元素列表，先得到(1, 384)矩阵，
    # 再用[0]取出第一行，得到(384,)向量。
    query_matrix = model.encode(
        [input_text],
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    query_vector = query_matrix[0]

    if query_vector.ndim != 1:
        raise ValueError("Query编码结果必须是一维向量")

    return query_vector


def search_top_k(
    documents: list[str],
    chunk_vectors: np.ndarray,
    query_vector: np.ndarray,
    top_k: int,
) -> tuple[
    np.ndarray,
    list[tuple[int, float, str]],
]:
    """计算相似度并返回降序排列的Top-K结果。"""
    if top_k <= 0:
        raise ValueError("top_k必须大于0")

    if chunk_vectors.ndim != 2:
        raise ValueError("Chunk向量必须是二维矩阵")

    if query_vector.ndim != 1:
        raise ValueError("Query向量必须是一维向量")

    if len(documents) != chunk_vectors.shape[0]:
        raise ValueError("文档数量与Chunk向量数量不一致")

    if chunk_vectors.shape[1] != query_vector.shape[0]:
        raise ValueError("Chunk与Query向量维度不一致")

    scores = chunk_vectors @ query_vector

    result_count = min(
        top_k,
        len(documents),
    )

    top_indices = np.argsort(
        -scores,
        kind="stable",
    )[:result_count]

    results = [
        (
            int(index),
            float(scores[index]),
            documents[index],
        )
        for index in top_indices
    ]

    return scores, results


def print_results(
    results: list[tuple[int, float, str]],
) -> None:
    """打印已经完成排序的检索结果。"""
    for rank, (index, score, text) in enumerate(
        results,
        start=1,
    ):
        print(
            f"第{rank}名 | "
            f"index={index} | "
            f"score={score:.6f} | "
            f"{text}"
        )


def main() -> None:
    model = SentenceTransformer(
        MODEL_NAME,
        device="cpu",
    )

    # Passage只需要提前编码一次。
    chunk_vectors = encode_passages(
        model,
        DOCUMENTS,
    )

    print("Chunk矩阵形状:", chunk_vectors.shape)

    print("\n========== 四个查询的Top-2 ==========")

    for query_number, (
        query,
        expected_index,
    ) in enumerate(
        zip(
            QUERIES,
            EXPECTED_TOP_INDICES,
        ),
        start=1,
    ):
        query_vector = encode_query(
            model,
            query,
        )

        scores, results = search_top_k(
            DOCUMENTS,
            chunk_vectors,
            query_vector,
            top_k=2,
        )

        print(f"\n查询{query_number}: {query}")
        print("Query向量形状:", query_vector.shape)
        print("分数形状:", scores.shape)

        print_results(results)

        actual_index = results[0][0]

        if actual_index == expected_index:
            print("检查结果: 预期文本排在第一")
        else:
            print(
                "检查结果: 第一名与预期不同，"
                f"预期index={expected_index}，"
                f"实际index={actual_index}"
            )

    print("\n========== 不同top_k ==========")

    test_query = QUERIES[0]
    test_query_vector = encode_query(
        model,
        test_query,
    )

    for top_k in [1, 3, 10]:
        _, results = search_top_k(
            DOCUMENTS,
            chunk_vectors,
            test_query_vector,
            top_k=top_k,
        )

        print(
            f"\n查询: {test_query}\n"
            f"设置top_k={top_k}，"
            f"实际返回{len(results)}条"
        )

        print_results(results)

    print("\n========== 空查询检查 ==========")

    try:
        encode_query(
            model,
            "   ",
        )
    except ValueError as error:
        print("成功拒绝空查询:", error)
    else:
        raise AssertionError("程序没有拒绝空查询")

    print("\n========== E5前缀对比 ==========")

    comparison_query = QUERIES[0]

    # 正确方式：Query和Passage使用对应前缀
    correct_query_vector = encode_query(
        model,
        comparison_query,
        use_prefix=True,
    )

    _, correct_results = search_top_k(
        DOCUMENTS,
        chunk_vectors,
        correct_query_vector,
        top_k=len(DOCUMENTS),
    )

    # 实验方式：Query和Passage都不添加前缀
    no_prefix_chunk_vectors = encode_passages(
        model,
        DOCUMENTS,
        use_prefix=False,
    )

    no_prefix_query_vector = encode_query(
        model,
        comparison_query,
        use_prefix=False,
    )

    _, no_prefix_results = search_top_k(
        DOCUMENTS,
        no_prefix_chunk_vectors,
        no_prefix_query_vector,
        top_k=len(DOCUMENTS),
    )

    print(f"\n查询: {comparison_query}")

    print("\n使用正确前缀:")
    print_results(correct_results)

    print("\n不使用前缀:")
    print_results(no_prefix_results)

    print(
        "\n说明：前缀实验只用于观察差异，"
        "正式检索仍应使用query:和passage:。"
    )


if __name__ == "__main__":
    main()