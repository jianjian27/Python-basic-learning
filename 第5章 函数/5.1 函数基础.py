# 函数定义
def out_line():
    print("-------")

out_line()

# 函数的参数与返回值
def rectangle_area(l,w):
    area = l * w
    return area

def circle_area_len(r):
    return 3.14 * r**2,2 * 3.14 * r# 多个返回值，逗号分开
al = circle_area_len(5)# 多个返回值会封装到元组之中
print(al)

