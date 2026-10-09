# 向量和矩阵形状
# → 向量归一化
# → 余弦相似度
# → 批量矩阵计算
# → Top-K排序
# → 分数与原文对应

import numpy as np


def normalize_vector(vector: np.ndarray) -> np.ndarray:
    """归一化一个一维向量。"""
    length = np.linalg.norm(vector)

    if length == 0:
        raise ValueError("不能归一化零向量。")

    return vector / length

def normalize_rows(matrix: np.ndarray) -> np.ndarray:
    """分别归一化二维矩阵中的每一行。"""
    lengths = np.linalg.norm(
        matrix,
        axis=1,
        keepdims=True,
    )

    if np.any(lengths == 0):
        raise ValueError("不能归一化包含零向量的矩阵。")

    return matrix / lengths

def search(
        documents: list[str],
        chunk_vectors: np.ndarray,
        query_vector: np.ndarray,
        top_k: int,
) -> list[tuple[str, float]]:
    if len(documents) != chunk_vectors.shape[0]:
        raise ValueError("文档数量必须等于Chunk向量数量")

    if chunk_vectors.shape[1] != query_vector.shape[0]:
        raise ValueError("Chunk向量与查询向量的维度不一致")

    if top_k <= 0:
        raise ValueError("top_k必须大于0。")

    chunk_vectors = normalize_rows(chunk_vectors)
    query_vector = normalize_vector(query_vector)
    scores = chunk_vectors @ query_vector
    result_count = min(top_k, len(documents))
    top_indices = np.argsort(scores)[::-1][:result_count]

    return [(documents[i], float(scores[i])) for i in top_indices]



documents = [
    "论文使用李雅普诺夫函数证明系统稳定。",
    "数值实验采用四阶Runge-Kutta方法。",
    "本文研究忆阻神经网络的同步控制。",
    "论文介绍了非线性系统的研究背景。",
]

chunk_vectors = np.array([
    [3.0, 4.0, 0.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 1.0],
    [-1.0, 0.0, 0.0],
])

query_vector = np.array([1.0, 1.0, 0.0])

results = search(
    documents,
    chunk_vectors,
    query_vector,
    top_k=2,
)

for text, score in results:
    print(score, text)

normalized_chunks = normalize_rows(chunk_vectors)
normalized_query = normalize_vector(query_vector)

assert len(documents) == chunk_vectors.shape[0]
assert chunk_vectors.shape[1] == query_vector.shape[0]
assert np.allclose(
    np.linalg.norm(normalized_chunks, axis=1),
    1.0,
)


scores = normalized_chunks @ normalized_query

top_k = 2

if top_k <= 0:
    raise ValueError("top_k必须大于0。")

result_count = min(top_k, len(documents))
top_indices = np.argsort(scores)[::-1][:result_count]

print("Chunk矩阵形状: ", chunk_vectors.shape)
print("查询向量形状: ", query_vector.shape)
print("分数形状: ", scores.shape)

print("\n全部结果: ")

for index, score in enumerate(scores):
    print(index, float(scores[index]), documents[index])