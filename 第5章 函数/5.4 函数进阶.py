# 函数变量的作用域
# 全局变量:在函数之外定义的变量,称之为全局变量,在整个文件中(包括函数内)都可以使用,通常定义在文件的顶部
# 局部变量:在函数内部定义的变量,称之为局部变量,只能在该函数内部使用,外部无法访问,函数执行完毕后,会自动销毁其内部局部变量

# global关键字,用于明确告诉Python解释器,在函数中要使用全局变量,使得可以在函数内部修改全局变量的值
# num = 100
# def rectangle_area(l,w):
#     area = l * w
#     global num
#     num = 10000
#     return area
# rectangle_area(1,2)
# print(num)

# 尽量避免在函数中使用全局变量，难以维护和调试
# global主要用在程序的状态，配置和计数器，例如记录某函数调用的次数等场景中

# 递归调用：在函数中调用自己的情况，先层层递进至终结点，再逐层回归
# 递归调用，一定要有终结点
def mul(n):
    if n == 1:
        return 1
    else:
        return n * mul(n - 1)

a = int(input("num:"))
print(mul(a))

def cal_order_cost(*args:tuple[str,float,int],coupon = 0,score = 0,express = 0.0)->float:
    """
    根据传入的一批商品信息（商品名，价格，数量），优惠（优惠券，积分抵扣），运费信息计算订单的总金额
    :param args:商品信息（商品名，价格，数量），（“鼠标”，188,2）（“键盘”，388,1）
    :param coupon:优惠券
    :param score:积分抵扣
    :param express:运费信息
    :return:订单总金额
    """
    #订单总金额 = 商品总金额 - 优惠券 -积分抵扣 + 运费
    #1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    #2.扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost and score // 100 <= total_cost:
        total_cost = total_cost - coupon
    #3.扣减积分抵扣
        total_cost = total_cost - score // 100
    #4.添加运费
    total_cost = total_cost + express

    return total_cost

total = cal_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),coupon = 10,score = 4000,express = 9.9)
print(total)