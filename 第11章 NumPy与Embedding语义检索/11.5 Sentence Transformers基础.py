import numpy as np
from sentence_transformers import SentenceTransformer


MODEL_NAME = "intfloat/multilingual-e5-small"

documents = [
    "本文使用李雅普诺夫函数证明系统稳定。",
    "数值实验采用四阶Runge-Kutta方法。",
    "本文研究忆阻神经网络的同步控制。",
]

model = SentenceTransformer(MODEL_NAME, device="cpu",)

passage_texts = [
    f"passage: {document}"
    for document in documents
]

vectors = model.encode(
    passage_texts,
    batch_size=2,
    show_progress_bar=True,
    convert_to_numpy=True,
    normalize_embeddings=True,
)

print("结果类型：", type(vectors))
print("向量数据类型：", vectors.dtype)
print("向量矩阵形状：", vectors.shape)
print("模型向量维度：",model.get_embedding_dimension())

lengths = np.linalg.norm(vectors, axis=1)

print("各向量长度：", lengths)
print("第一个向量前5维：", vectors[0][:5])

assert isinstance(vectors, np.ndarray)
assert vectors.shape[0] == len(documents)
assert vectors.shape[1] == model.get_embedding_dimension()
assert np.allclose(lengths, 1.0, atol=1e-5)

similarities = vectors @ vectors.T

print("相似度矩阵：")
print(similarities)

assert similarities.shape == (
    len(documents),
    len(documents),
)

assert np.allclose(
    np.diag(similarities),
    1.0,
    atol=1e-5,
)

assert np.allclose(
    similarities,
    similarities.T,
    atol=1e-6,
)

single_vector = model.encode(
    passage_texts[0],
    normalize_embeddings=True,
)

one_vector_matrix = model.encode(
    [passage_texts[0]],
    normalize_embeddings=True,
)

print("单个字符串形状:", single_vector.shape)
print("单元素列表形状:", one_vector_matrix.shape)

assert single_vector.shape == (384,)
assert one_vector_matrix.shape == (1, 384)