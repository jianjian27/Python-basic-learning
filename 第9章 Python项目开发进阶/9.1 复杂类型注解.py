# 类型注解：为变量、函数参数和返回值指定数据类型，以提高代码的可读性和可维护性。
# 提前发现潜在的类型错误，减少运行时错误的发生。
# 描述函数的输入和输出类型，帮助开发者理解函数的使用方式。
# 在大型项目中明确模块之间的数据约定，有助于团队协作和代码审查，提高代码质量。
# 类型注解不会自动进行类型检查，但可以与静态类型检查工具（如mypy）结合使用，提供更严格的类型检查。

from typing import Iterator # 生成器

# 变量类型注解 变量名: 类型 = 值
page: int = 3
title: str = "稳定性分析"
similarity: float = 0.87
indexed: bool = True

# 容器类型注解

# 列表
page_numbers: list[int] = [
    1,
    2,
    3,
]# page_numbers是一个列表，列表中的每个元素都是整数类型。

# list[int]
# list[str]
# list[float]
# list[Section]# 列表中放自定义的对象

# 集合
keywords: set[str] = {
    "混沌",
    "稳定性",
    "同步",
}# keywords是一个集合，集合中的每个元素都是字符串类型。

# 字典
page_texts: dict[int, str] = {
    1: "第一页正文",
    2: "第二页正文",
}# page_texts是一个字典，字典的键是整数类型，值是字符串类型。

section_pages: dict[str, list[int]] = {
    "引言": [1, 2],
    "数学模型": [3, 4, 5],
}#嵌套类型，从内往外阅读dict[str, list[int]]

# 元组
# 固定结构元组
paper_info: tuple[str, int] = (
    "论文标题",
    2026,
)

# 任意长度的同类型元组
section_path: tuple[str, ...] = (
    "第三章",
    "3.2 稳定性分析",
)# ...表示同一类型可以重复任意次数

# 单元素元组需要注意末尾逗号
path = ("第一章",)
# 如果不加逗号，Python会将其解释为字符串
path = ("第一章")
path = "第一章"

# 联合类型与可空类型
number: str | None = None# number可以是字符串类型，也可以是None，表示该变量可能没有值.
result: int | float

# 自定义类型
class Section:# 自己定义的类也可以作为类型
    def _init_(self, title: str):
        self.tetile = title
section: Section = Section(
    "数学模型",
)
sections: list[Section] = [
    Section("引言"),
    Section("数学模型"),
    Section("结论")
]

# 理解Iterator[T]
# Iterator[T]表示一个生成器，它会产生类型为T的值。
Iterator[
    tuple[
        Section,
        tuple[str, ...],
    ]
]# 一个迭代器，每次产生一个二元素元组；元组的第一项是章节对象，第二项是由字符串组成的完整章节路径。

def iter_sections_with_paths(
    sections: list[Section],
    parent_path: tuple[str, ...] = (),
) -> Iterator[
    tuple[
        Section,
        tuple[str, ...],
    ]
]:
    pass