import unittest
from abc import ABC, abstractmethod
from unittest.mock import Mock

import numpy as np
from sentence_transformers import SentenceTransformer


class TextEncoder(ABC):
    """文本编码器抽象接口。"""

    @abstractmethod
    def encode_queries(
        self,
        texts: list[str],
    ) -> np.ndarray:
        raise NotImplementedError

    @abstractmethod
    def encode_passages(
        self,
        texts: list[str],
    ) -> np.ndarray:
        raise NotImplementedError


class SentenceTransformerEncoder(TextEncoder):
    """为E5添加前缀并调用底层模型。"""

    def __init__(
        self,
        model: SentenceTransformer,
        *,
        batch_size: int = 32,
    ) -> None:
        if batch_size <= 0:
            raise ValueError("batch_size 必须大于0")

        self._model = model
        self._batch_size = batch_size

    @property
    def embedding_dimension(self) -> int:
        dimension = (
            self._model.get_embedding_dimension()
        )

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

        vectors = np.asarray(vectors, dtype=np.float32,)

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
            raise RuntimeError(
                "向量数量与文本数量不一致"
            )

        if (
            vectors.shape[1] != self.embedding_dimension
        ):
            raise RuntimeError("编码结果维度与模型维度不一致")

        lengths = np.linalg.norm(vectors, axis=1)

        if not np.allclose(
            lengths,
            1.0,
            atol=1e-5,
        ):
            raise RuntimeError("编码结果没有正确归一化")


class SemanticRetriever:
    """依赖TextEncoder的语义检索器。"""

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
                documents
            )
        )

        query_matrix = (
            self._encoder.encode_queries(
                [query]
            )
        )

        query_vector = query_matrix[0]

        if (
            chunk_vectors.ndim != 2
            or query_vector.ndim != 1
        ):
            raise RuntimeError("向量形状不正确")

        if (
            chunk_vectors.shape[0]
            != len(documents)
        ):
            raise RuntimeError(
                "向量数量与文档数量不一致"
            )

        if (
            chunk_vectors.shape[1]
            != query_vector.shape[0]
        ):
            raise RuntimeError(
                "Chunk与Query维度不一致"
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


class SentenceTransformerEncoderTests(
    unittest.TestCase
):
    def setUp(self) -> None:
        self.model = Mock(
            spec=SentenceTransformer
        )

        self.model.get_embedding_dimension.return_value = 2

        self.encoder = SentenceTransformerEncoder(
            self.model,
            batch_size=2,
        )

    def test_queries_receive_query_prefix(
        self,
    ) -> None:
        expected = np.array([
            [1.0, 0.0],
            [0.0, 1.0],
        ], dtype=np.float32)

        self.model.encode.return_value = expected

        actual = self.encoder.encode_queries([
            "如何证明系统稳定？",
            "使用了什么数值方法？",
        ])

        self.model.encode.assert_called_once_with(
            [
                "query: 如何证明系统稳定？",
                "query: 使用了什么数值方法？",
            ],
            batch_size=2,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        np.testing.assert_array_equal(
            actual,
            expected,
        )

    def test_passages_receive_passage_prefix(
        self,
    ) -> None:
        expected = np.array([
            [1.0, 0.0],
            [0.0, 1.0],
        ], dtype=np.float32)

        self.model.encode.return_value = expected

        self.encoder.encode_passages([
            "李雅普诺夫函数证明稳定。",
            "采用Runge-Kutta方法。",
        ])

        self.model.encode.assert_called_once_with(
            [
                "passage: 李雅普诺夫函数证明稳定。",
                "passage: 采用Runge-Kutta方法。",
            ],
            batch_size=2,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

    def test_empty_list_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.encoder.encode_queries([])

        self.model.encode.assert_not_called()

    def test_blank_text_is_rejected(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            self.encoder.encode_passages([
                "有效文本",
                "   ",
            ])

        self.model.encode.assert_not_called()

    def test_wrong_row_count_is_rejected(
        self,
    ) -> None:
        self.model.encode.return_value = np.array([
            [1.0, 0.0],
        ], dtype=np.float32)

        with self.assertRaises(RuntimeError):
            self.encoder.encode_queries([
                "查询一",
                "查询二",
            ])

    def test_wrong_dimension_is_rejected(
        self,
    ) -> None:
        self.model.encode.return_value = np.array([
            [1.0, 0.0, 0.0],
        ], dtype=np.float32)

        with self.assertRaises(RuntimeError):
            self.encoder.encode_queries([
                "查询",
            ])

    def test_non_normalized_vectors_are_rejected(
        self,
    ) -> None:
        self.model.encode.return_value = np.array([
            [3.0, 4.0],
        ], dtype=np.float32)

        with self.assertRaises(RuntimeError):
            self.encoder.encode_queries([
                "查询",
            ])


class SemanticRetrieverTests(
    unittest.TestCase
):
    def test_retriever_uses_injected_encoder(
        self,
    ) -> None:
        documents = [
            "稳定性证明",
            "数值实验",
            "研究背景",
        ]

        encoder = Mock(
            spec=TextEncoder
        )

        encoder.encode_passages.return_value = (
            np.array([
                [1.0, 0.0],
                [0.0, 1.0],
                [-1.0, 0.0],
            ])
        )

        encoder.encode_queries.return_value = (
            np.array([
                [1.0, 0.0],
            ])
        )

        retriever = SemanticRetriever(
            encoder
        )

        results = retriever.search(
            documents,
            "如何证明系统稳定？",
            top_k=2,
        )

        encoder.encode_passages.assert_called_once_with(
            documents
        )

        encoder.encode_queries.assert_called_once_with(
            ["如何证明系统稳定？"]
        )

        self.assertEqual(
            results[0][0],
            "稳定性证明",
        )

        self.assertAlmostEqual(
            results[0][1],
            1.0,
        )

        self.assertEqual(
            results[1][0],
            "数值实验",
        )

        self.assertAlmostEqual(
            results[1][1],
            0.0,
        )


if __name__ == "__main__":
    unittest.main(
        verbosity=2,
    )