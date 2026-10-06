# 1. Python 列表与 NumPy 数组

# Python 列表更像通用容器：
# python_list = [1.0, 2.0, 3.0]
# NumPy 数组用于数值计算：
# import numpy as np
#
# vector = np.array([1.0, 2.0, 3.0])

# 关键区别：
# - 列表可以混合保存多种类型；
# - NumPy 数组通常使用统一的元素类型；
# - NumPy 支持向量、矩阵和批量运算；
# - Embedding 模型通常返回 NumPy 数组或相似的张量结构。
# 例如：
# python_list = [1, 2, 3]
#
# print(python_list * 2)
# # [1, 2, 3, 1, 2, 3]
# 而：
# numpy_array = np.array([1, 2, 3])
#
# print(numpy_array * 2)
# # [2 4 6]
# 列表的 * 2 是重复内容，NumPy 数组的 * 2 是逐元素乘法。

# 2. 创建一维数组
# import numpy as np
#
# vector = np.array([1.0, 2.0, 3.0])
#
# print(vector)
# print(vector.shape)
# print(vector.ndim)
# print(vector.dtype)
# 含义：
# - np.array(...)：把列表转换成 NumPy 数组；
# - vector.shape：数组各个维度的长度；
# - vector.ndim：数组有几个维度；
# - vector.dtype：数组元素的数据类型。
# 预期结果类似：
# [1. 2. 3.]
# (3,)
# 1
# float64
# (3,) 表示它是一维数组，其中有三个元素。
# 注意：(3,) 只是一个一维向量，并没有明确区分“行向量”和“列向量”。

# 3. 创建二维数组
# matrix = np.array([
#     [1.0, 2.0],
#     [3.0, 4.0],
#     [5.0, 6.0],
# ])
#
# print(matrix.shape)
# print(matrix.ndim)
# print(matrix.dtype)
# 预期结果：
# (3, 2)
# 2
# float64
# shape == (3, 2) 表示：
# 3 行
# 2 列
# Embedding 检索中，如果有三个文本、每个文本被编码成二维向量，那么它们组成的矩阵也会是 (3, 2)。

# 4. 访问元素、行和列
# matrix = np.array([
#     [1.0, 2.0],
#     [3.0, 4.0],
#     [5.0, 6.0],
# ])
# 访问单个元素：
# print(matrix[1, 0])
# # 3.0

# NumPy 使用从零开始的索引：
# matrix[行索引, 列索引]
# 因此 matrix[1, 0] 是第二行、第一列。
# 访问整行：
# print(matrix[1])
# # [3. 4.]
# 访问整列：
# print(matrix[:, 0])
# # [1. 3. 5.]
# 这里的 : 表示选取该维度的全部内容，所以 matrix[:, 0] 表示“所有行的第零列”。

# 5. 理解 dtype
# integers = np.array([1, 2, 3])
# floats = np.array([1.0, 2.0, 3.0])
#
# print(integers.dtype)
# print(floats.dtype)
# 输出通常类似：
# int64
# float64
# Embedding 向量由小数组成，常见类型包括：
# float32
# float64
# NumPy 会尽量统一数组中的元素类型：
# mixed = np.array([1, 2.5, 3])
#
# print(mixed)
# print(mixed.dtype)
# 整数会被转换为浮点数：
# [1.  2.5 3. ]
# float64

# 6. 创建特殊数组
# 创建零向量：
# zero_vector = np.zeros(384)
#
# print(zero_vector.shape)
# # (384,)
# 创建三行四列的零矩阵：
# matrix = np.zeros((3, 4))
#
# print(matrix.shape)
# # (3, 4)
# 注意参数区别：
# np.zeros(384)       # 一维数组
# np.zeros((3, 4))    # 二维数组，需要用元组表示形状

import numpy as np

zero_vector = np.zeros(384)

matrix = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
])

print(zero_vector.shape)
print(zero_vector.ndim)
print(zero_vector.dtype)

rows, columns = matrix.shape
print("行数：", rows)
print("列数：", columns)

print("第二行：", matrix[1])
print("第三列：", matrix[:, 2])
