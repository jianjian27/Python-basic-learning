# 函数的说明文档（Docstring）是写在函数开头，用三个引号包裹的字符串，用于解释函数的功能，参数，返回值等信息，
# 方便调用者清楚函数的具体作用及细节
def rectangle_area(l,w):
    """
    根据给出的长宽计算长方形面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形面积
    """
    area = l * w
    return area
help(rectangle_area)
# 也可鼠标光标放在函数上即可显示函数说明文档