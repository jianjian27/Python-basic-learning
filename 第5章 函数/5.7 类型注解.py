# 类型注解是Python中的一种语法特性，用于明确标识变量，函数参数，和返回值的数据类型，从而使代码更清晰，更安全，更易维护
# 定义变量
import math

a: int = 695

score: float = 98.5

hobby: str = "Python"

flag: bool = True

pic: None = None


names: list[str] = ["A", "C", "E"]

phones: set[str] = {"13309091111", "15209109121"}

options: dict[str, int] = {"count": 0, "total": 0}

goods: tuple[str, int, int] = ("手机", 5999, 1)

# 函数的类型注解
def circle_area_len(r: float) -> tuple[float,float]:
    return round(3.14 * r * r, 1),round(2 * 3.14 * r, 1)

