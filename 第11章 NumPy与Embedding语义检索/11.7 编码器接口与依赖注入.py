# 抽象接口
# Python 可以用 ABC 和 @abstractmethod 定义这种接口。抽象类不能直接实例化，子类必须实现所有抽象方法

from abc import ABC, abstractmethod

import numpy as np
from sentence_transformers import SentenceTransformer


MODEL_NAME = "intfloat/multilingual-e5-small"


# TextEncoder 只规定 encode_queries()和 encode_passages()两个方法的接口
# 没有规定使用什么模型，是否使用 PyTorch，是否需要联网，向量有多少维，内部如何添加前缀等
# 它描述的是“编码器必须会做什么 ”，而不是“具体怎么做 ” 。
# encoder = TextEncoder() 不能运行，无法实例化抽象类，因为TextEncoder含有尚未实现的抽象方法。
# 只有实现了两个方法的具体子类才能实例化，例如 SentenceTransformerEncoder。
class TextEncoder(ABC):
    """文本编码器抽象接口。"""

    @abstractmethod
    def encode_queries(
        self,
        texts: list[str],
    ) -> np.ndarray:
        """将查询文本编码为二维向量矩阵。"""
        raise NotImplementedError

    @abstractmethod
    def encode_passages(
        self,
        texts: list[str],
    ) -> np.ndarray:
        """将候选原文编码为二维向量矩阵。"""
        raise NotImplementedError


class SentenceTransformerEncoder(TextEncoder):
    """基于 Sentecnce Transformers 和 E5 的编码器。"""

    def __init__(
        self,
        model_name: str,
        *,
        device: str = "cpu",
        batch_size: int = 32,
    ) -> None:
        if not model_name.strip():
            raise ValueError("模型名称不能为空")

        if batch_size <= 0:
            raise ValueError("batch_size 必须大于0")

        self._model_name = model_name
        self._batch_size = batch_size

        self._model = SentenceTransformer(
            model_name,
            device = device,
        )

    @property
    def model_name(self) -> str:
        return self._model_name

    @property
    def embedding_dimension(self) -> int:
        dimension = self._model.get_embedding_dimension()

        if dimension is None:
            raise RuntimeError("模型没有提供向量维度")

        return dimension

    def encode_queries(
        self,
        texts: list[str],
    ) -> np.ndarray:
        return self._encode(
            texts,
            prefix="query: ",
        )

    def encode_passages(
        self,
        texts: list[str],
    ) -> np.ndarray:
        return self._encode(
            texts,
            prefix="passage: ",
        )

    def _encode(
        self,
        texts: list[str],
        *,
        prefix: str,
    ) -> np.ndarray:
        self._validate_texts(texts)

        model_inputs = [
            f"{prefix}{text.strip()}"
            for text in texts
        ]

        vectors = self._model.encode(
            model_inputs,
            batch_size=self._batch_size,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        vectors = np.asarray(
            vectors,
            dtype=np.float32,
        )

        self._validate_vectors(
            vectors,
            expected_rows=len(texts),
        )

        return vectors

    @staticmethod
    def _validate_texts(
        texts: list[str],
    ) -> None:
        if not texts:
            raise ValueError("待编码文本不能为空")

        if any(not text.strip() for text in texts):
            raise ValueError("待编码文本不能包含空字符串")

    def _validate_vectors(
        self,
        vectors: np.ndarray,
        *,
        expected_rows: int,
    ) -> None:
        if vectors.ndim != 2:
            raise RuntimeError("编码结果必须是二维矩阵")

        if vectors.shape[0] != expected_rows:
            raise RuntimeError("向量数量与文本数量不一致")

        if vectors.shape[1] != self.embedding_dimension:
            raise RuntimeError("编码结果维度与模型维度不一致")

        lengths = np.linalg.norm(
            vectors,
            axis=1,
        )

        if not np.allclose(
            lengths,
            1.0,
            atol=1e-5,
        ):
            raise RuntimeError("编码结果没有正确归一化")

class SemanticRetriever:
    """只依赖 TextEncoder 接口的语义检索器。"""

    def __init__(
        self,
        encoder: TextEncoder,
    ) -> None:
        self._encoder = encoder

    def search(
        self,
        documents: list[str],
        query: str,
        *,
        top_k: int,
    ) -> list[tuple[str, float]]:
        if not documents:
            raise ValueError("候选文档不能为空")

        if not query.strip():
            raise ValueError("查询文本不能为空")

        if top_k <= 0:
            raise ValueError("top_k必须大于0")

        chunk_vectors = (
            self._encoder.encode_passages(
                documents,
            )
        )

        query_matrix = (
            self._encoder.encode_queries(
                [query],
            )
        )

        query_vector = query_matrix[0]

        if (
            chunk_vectors.shape[1]
            != query_vector.shape[0]
        ):
            raise RuntimeError(
                "Chunk与Query向量维度不一致"
            )

        scores = (
            chunk_vectors
            @ query_vector
        )

        result_count = min(
            top_k,
            len(documents),
        )

        top_indices = np.argsort(
            -scores,
            kind="stable",
        )[:result_count]

        return [
            (
                documents[index],
                float(scores[index]),
            )
            for index in top_indices
        ]


def main() -> None:
    documents = [
        "本文使用李雅普诺夫函数证明系统稳定。",
        "数值实验采用四阶Runge-Kutta方法。",
        "本文研究忆阻神经网络的同步控制。",
        "论文介绍了非线性系统的研究背景。",
    ]

    query = "论文如何证明系统稳定？"

    encoder = SentenceTransformerEncoder(
        MODEL_NAME,
        device="cpu",
        batch_size=2,
    )

    # 依赖注入：SemanticRetriever 没有自己创建编码器，而是由外部把编码器传入构造函数。
    # 这使得 SemanticRetriever 可以使用任何实现了 TextEncoder 接口的编码器，而不局限于 SentenceTransformerEncoder。
    # 这叫构造函数依赖注入，因为依赖对象在构造函数中被注入。
    # 如果不使用依赖注入，SemanticRetriever 可能会直接在内部创建一个 SentenceTransformerEncoder，检索器就知道了具体模型实现。
    # 使用依赖注入后，检索器只知道它有一个编码器，它只关心编码器能做什么，而不关心编码器具体怎么实现，只依赖抽象接口。
    retriever = SemanticRetriever(encoder,)

    results = retriever.search(
        documents,
        query,
        top_k=2,
    )

    print("模型：", encoder.model_name)
    print("向量维度：", encoder.embedding_dimension)

    for rank, (text, score) in enumerate(results, start=1,):
        print(
            f"第{rank}名 | "
            f"score={score:.6f} | "
            f"{text}"
        )


if __name__ == "__main__":
    main()
