# @dataclass数据类可以自动生成一些特殊方法，比如__init__()、__repr__()、__eq__()等，从而简化类的定义。
from dataclasses import (dataclass, field,)

@dataclass
class Paper:# 使用了装饰器语法，可以理解为类定义完成后，让dataclass帮忙加工这个类，为它生成常见方法
    title: str
    year: int

first = Paper(title = "忆阻神经网络研究", year = 2027,)
print(first)
# @dataclass自动生成了适合数据对象使用的__init__()方法，允许我们在创建实例时直接传入属性值。

# field()是从dataclasses模块中导入的一个函数，它的作用是为某个数据类字段提供更详细的配置
children: list[str] = field(
    default_factory=list
)# children是一个字符串列表字段，按照field()中的配置生成它

@dataclass
class Section:
    title: str
    children: list[str] = field(
        default_factory=list
    )# 告诉dataclass:字段名称children，字段类型list[str]，默认值生成方式是调用list()函数创建一个空列表。
first = Section("第一章")# 创建对象时，dataclass发现没有提供children参数，就调用list()函数生成一个空列表作为默认值。

# frozen=True 表示对象创建后，不允许重新修改字段
@dataclass(frozen=True)
class Chunk:
    id: str
    content: str

chunk = Chunk(id="chunk-1", content="这是一个不可变的块对象")
# chunk.id = "chunk-2"  # 这行代码会引发错误

# @property把简单、快速、没有明显副作用的计算结果表现成属性.
@dataclass(frozen=True)
class Paper:
    title: str
    year: int

    @property
    def display_name(self) -> str:
        return f"{self.title}（{self.year}）"

paper = Paper(
    title="混沌系统研究",
    year=2025,
)
print(paper.display_name)# 无需括号

# _post_init_()方法是dataclass在实例化对象后自动调用的一个特殊方法，它允许我们在对象创建后进行额外的初始化操作。
# 比如我们希望对象创建后立即检查数据，可以在_post_init_()中实现。
@dataclass
class Paper:
    title: str
    year: int

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError(
                "论文标题不能为空。"
            )

        if self.year <= 0:
            raise ValueError(
                "年份必须大于 0。"
            )
# paper = Paper(
#    title="",
#    year=2025,
#)会在创建对象时触发_post_init_()方法，抛出ValueError异常，提示标题不能为空。

from dataclasses import asdict # 转换成字典，在写入数据库或转换为JSON格式时非常有用。

paper_dict = asdict(paper)
print(paper_dict)  # 输出: {'title': '混沌系统研究', 'year': 2025}

