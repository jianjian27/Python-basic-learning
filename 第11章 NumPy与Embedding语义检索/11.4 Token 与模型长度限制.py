# 模型不能直接处理字符串，而是先通过 tokenizer 将文本拆成 Token，再转换成整数 ID：
# 原始文本
# → Tokenizer
# → Token序列
# → Token ID
# → Embedding模型
# → 文本向量
# 例如：
# 本文使用李雅普诺夫函数证明系统稳定。
# 可能被拆成若干汉字、词语或子词，但具体结果完全取决于模型使用的 tokenizer。
# 因此不能假设：
# 1个汉字 = 1个Token
# 1个英文单词 = 1个Token

# 字符、单词和 Token 不相同
# 字符数
# Python 可以直接计算：
# text = "本文使用李雅普诺夫函数。"
#
# print(len(text))
# 这是 Python 字符串长度，不是 Token 数。
# 英文单词数
# text = "The system is asymptotically stable."
#
# print(len(text.split()))
# 用空格切分可以粗略计算英文单词，但不能计算真正的 Token。
# 例如一个较长或少见的英文单词可能被拆成多个子词 Token。
# 中文文本
# 中文通常不使用空格分词：
# text = "本文使用李雅普诺夫函数。"
#
# print(text.split())
# 结果只有一个字符串元素，因此不能通过 split() 统计中文词数或 Token 数。
# 数学文本
# 下面这些内容可能消耗不少 Token：
# x_1(t)
# D^αx(t)
# λ_max
# 式（17）
# 0.0001
# 符号、下标、标点和数字都可能被拆成不同 Token。因此论文中的公式密集文本尤其不能只根据字符数估计模型输入长度。
# 3. 使用真正的 tokenizer 计数
# 概念代码如下：
from transformers import AutoTokenizer

model_name = "intfloat/multilingual-e5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "passage: 本文使用李雅普诺夫函数证明系统稳定。"

encoded = tokenizer(
    text,
    add_special_tokens=True,
    truncation=False,
)

token_ids = encoded["input_ids"]
tokens = tokenizer.convert_ids_to_tokens(token_ids)

print("字符数: ", len(text))
print("Token数: ", len(token_ids))
print("Tokens: ", tokens)
