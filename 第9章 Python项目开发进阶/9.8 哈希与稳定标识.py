# 很多系统都需要快速判断两个对象是否 “相同 ”或 “发生变化 ”：
# 两个文件内容是否相同；
# 两个 Chunk 是否相同；
# 论文是否已经导入；
# Chunk 的 Embedding 是否需要重建；
# 数据库中是否已经存在某条内容；
# 同样输入是否应该生成同样的 ID。
# 直接比较整个文件或长文本当然可以，但可能成本较高。哈希提供了一种更紧凑的表示：
# 任意长度的数据
# → 哈希函数
# → 固定长度的摘要

# 哈希值可以理解为数据的 “指纹 ”，具有以下特点：
# 1. 唯一性：不同的输入数据应该产生不同的哈希值，尽管哈希函数可能会发生碰撞，但好的哈希函数会尽量减少碰撞的概率。
# 2. 固定长度：无论输入数据的大小如何，哈希值的长度都是固定的，这使得哈希值在存储和传输时更加高效。
# 3. 快速计算：哈希函数的计算速度通常很快，适合在需要频繁比较数据的场景中使用。
# 4. 不可逆性：从哈希值无法还原出原始数据，这对于保护数据隐私和安全性非常重要。
# 5. 敏感性：“ 雪崩效应 ”,对输入数据的微小变化会导致哈希值发生显著变化，这使得哈希值可以用于检测数据的完整性和一致性。

from hashlib import sha256
# hashlib 处理的是字节而不是Python字符串，所以我们需要将字符串编码为字节。常用的编码方式是 UTF-8。
text = "同步控制"
digest = sha256(text.encode("utf-8")).hexdigest()
# text.encode("utf-8") 将字符串 text 编码为 UTF-8 字节序列，str -> bytes
# 然后传递给 sha256 函数进行哈希计算。
# 使用 hexdigest() 方法将哈希值转换为十六进制字符串表示。
# 也可以使用 digest() 方法获取原始的字节(bytes,32字节)表示，但通常我们更喜欢使用十六进制字符串，因为它更易于阅读和存储。

# hashlib和内置的hash()函数的区别：
# 内置 hash() 函数是 Python 内置的哈希函数，主要用于在 Python 中实现哈希表（如字典和集合）的内部机制。它的特点是：
# 1. 不同的 Python 版本和不同的运行环境中，hash() 函数的结果可能不同，因为 Python 默认启用了哈希随机化，因此它不适合用于跨平台的数据一致性验证。
# 2. 内置 hash() 函数主要用于 Python 的内部实现，而不是用于数据的持久化存储或跨平台的数据验证。

# 哈希不是加密，哈希通常不能还原原文
# SHA-256 可以用于判断内容是否变化但不能用于保护内容，密码存储有专门的加密算法和哈希算法（如 bcrypt、scrypt、Argon2 等）来保护密码安全。
# 不同输入理论上可能得到相同哈希

# 同样含义的文本如果格式不同，直接哈希会不同
# “同步控制” 和 “同步 控制” 如果业务上认为它们是相同的，那么在哈希之前需要对文本进行标准化处理，例如去除多余的空格、统一大小写等，以确保哈希值的一致性。

def stable_hash(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def build_stable_id(
    paper_id: str,
    chunk_index: int,
    section_path: tuple[str, ...],
    content: str,
) -> str:
    identity = "\x1f".join([paper_id, str(chunk_index), *section_path, stable_hash(content)])
    return stable_hash(identity)

first = stable_hash("同步控制")
second = stable_hash("同步控制")
changed = stable_hash("同步控制。")

print(first == second)
print(first == changed)
print(len(first))

first_id = build_stable_id(
    "paper-1",
    0,
    ("第1章",),
    "同步控制",
)

same_id = build_stable_id(
    "paper-1",
    0,
    ("第1章",),
    "同步控制",
)

changed_id = build_stable_id(
    "paper-1",
    0,
    ("第1章",),
    "同步控制。",
)

print(first_id == same_id)      # True
print(first_id == changed_id)   # False
