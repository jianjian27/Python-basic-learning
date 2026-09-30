# 在新序列中使用*展开已有序列

# 解包不仅是语法简写，还可以创建候选值进行试算，同时保留原状态
current_units = ["单元A", "单元B"]
candidate = [*current_units, "单元C"]

current_units.append("单元D")

print(current_units)
print(candidate)


parent_path = ("第2章", "2.3 数值方法")

path_a = (parent_path, "2.3.1 龙格—库塔法")# 不加*，path_a是一个二元素元组，第一项是一个元组，第二项是一个字符串。
path_b = (*parent_path, "2.3.1 龙格—库塔法")# 加*，path_b是一个三元素元组，三个字符串。

print(path_a)
print(path_b)
print(len(path_a))# 2
print(len(path_b))# 3

def extend_section_path(
        parent_path: tuple[str, ...],
        section_title: str,
) -> tuple[str, ...]:
    return (*parent_path, section_title)

print(extend_section_path((), "引言"))
print(extend_section_path(("第1章",), "1.1 背景"))
print(extend_section_path(("第1章", "1.2 模型"), "1.2.1 方程"))

# **解包字典，*展开序列中的元素，**展开映射中的键值对
base_config = {
    "top_k": 5,
    "timeout": 30,
}

rag_config = {
    **base_config,
    "rerank": True,
}

print(rag_config)

# 重复的键会被后面的值覆盖
default_config = {
    "top_k": 5,
    "timeout": 30,
}

custom_config = {
    **default_config,
    "top_k": 10,
}

def merge_rag_config(
    defaults: dict[str, object],
    overrides: dict[str, object],
) -> dict[str, object]:
    return {**defaults, **overrides}

defaults = {
    "top_k": 5,
    "timeout": 30,
    "rerank": False,
}

overrides = {
    "top_k": 8,
    "rerank": True,
}

result = merge_rag_config(defaults, overrides)

print(result)
print(defaults)
print(overrides)

def describe_retrieval(
        query: str,
        top_k: int,
        rerank: bool,
) -> str:
    return f"问题={query}，Top_k={top_k}，重排={rerank}"

tuple1 = ("混沌系统", 5, True)
print(describe_retrieval(*tuple1))# *解包元组

dict1 = {"query": "混沌系统", "top_k": 5, "rerank": True}
print(describe_retrieval(**dict1))# **解包字典

tuple2 =("混沌系统",)
dict2 = {"top_k": 5, "rerank": True}
print(describe_retrieval(*tuple2, **dict2))# 同时使用*,**调用

options = {
    "top_k": 10,
    "rerank": True,
}

# describe_retrieval(
#     "非线性系统的同步控制",
#     top_k=5,
#     **options,
# )# 将会报错，因为函数参数中已经有了top_k参数，而**options中也包含了top_k键，导致重复传参。

# 推导式：把 “循环收集结果” 写成表达式
sections = [
    {
        "title": "数学模型",
        "blocks": [
            {"page": 2, "source": "2:1", "text": "  状态方程  "},
            {"page": 3, "source": "3:1", "text": ""},
        ],
    },
    {
        "title": "实验",
        "blocks": [
            {"page": 5, "source": "5:2", "text": "  实验设置 "},
            {"page": 5, "source": "5:3", "text": "结果分析"},
        ],
    },
]

# 普通循环
texts = []
for section in sections:
    for block in section["blocks"]:
        text = block["text"].strip()
        if text:
            texts.append(text)

# 推导式
texts1 = [
    block["text"].strip()
    for section in sections
    for block in section["blocks"]
    if block["text"].strip()
]

# 普通循环
pages = []
for section in sections:
    for block in section["blocks"]:
        pages.append(block["page"])

# 推导式
# 列表推导式
pages1 = [
    block["page"]
    for section in sections
    for block in section["blocks"]
]
# 集合推导式，自动去重
unique_pages = {
    block["page"]
    for section in sections
    for block in section["blocks"]
}

print(unique_pages)

source_to_page = {}
for section in sections:
    for block in section["blocks"]:
        source_to_page[block["source"]] = block["page"]

# 字典推导式
source_to_page1 = {
    block["source"]: block["page"]
    for section in sections
    for block in section["blocks"]
}
print(source_to_page1)


clean_texts = [
    block["text"].strip()
    for section in sections
    for block in section["blocks"]
    if block["text"].strip()
]

print(clean_texts)

page_set = {
    block["page"]
    for section in sections
    for block in section["blocks"]
}

print(page_set)

pages = tuple(sorted(page_set))

pages = tuple(
    sorted(
        {
            block["page"]
            for section in sections
            for block in section["blocks"]
        }
    )
)

# 生成器表达式：不创建完整的列表，而是按需生成元素
source_iter = (
    block["source"]
    for section in sections
    for block in section["blocks"]
)# 采用圆括号

print(source_iter) # 运行结果<generator object ...>,不会立即生成完整结果，只有被消费时才会生成元素。print(next(source_iter))# 迭代器消费一个元素

# 当前不手动调用next()，把生成器交给dict.fromkeys()，它会自动迭代生成器，创建字典的键
source_blocks = tuple(
    dict.fromkeys(source_iter)
) # dict.fromkeys()与set()集合去重不同，集合只强调不重复，不依赖顺序。而dict.fromkeys()会保留第一次出现的顺序，后续重复的键会被忽略。

values = ["A", "B", "A", "C", "B"]
source_iter = (value for value in values)

print(tuple(dict.fromkeys(source_iter)))

source_to_page = {
    block["source"]: block["page"]
    for section in sections
    for block in section["blocks"]
}
