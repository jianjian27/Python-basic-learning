# 添加修改均为直接写键值对，若原字典内没有则添加，若有则修改
# 字典名称pop(key)，删除制定的key，并返回key对应的value,del也可
# 字典名称[key]根据key获取value
# 字典名称.get(key)根据key获取value
# 字典名称.keys()获取所有的key
# 字典名称.values()获取所有的value
# 字典名称.items()获取所有的键值对

shopping_cart = {}
print("welcome")
menu = """
### shopping system ###
#        1.add        #
#        2.remove     #  
#        3.delete     #  
#        4.serch      #  
#        5.out        #
#######################
"""
print(menu)
while True:
    choice = input("please enter your choice:")
    match choice:
        case"1":
            goods_name = input("please enter goods name:")
            if goods_name in shopping_cart.keys():
                print("repeat")
            else:
                goods_price = float(input("please enter goods price:"))
                goods_amount = int(input("please enter goods amount:"))
                shopping_cart[goods_name] = {"price":goods_price,"amount":goods_amount}
                print("have been added")
        case"2":
            goods_name = input("please enter goods name:")
            if goods_name in shopping_cart:
                print(shopping_cart[goods_name])
                goods_price = float(input("please enter goods new price:"))
                goods_amount = int(input("please enter goods new amount:"))
                shopping_cart[goods_name] = {"price":goods_price,"amount":goods_amount}
                print("have been changed")
            else:
                print("please add this goods first")
        case"3":
            goods_name = input("please enter goods name:")
            if goods_name in shopping_cart:
                del shopping_cart[goods_name]
                print("have been deleted")
            else:
                print("please add this goods first")
        case"4":
          for goods_name in shopping_cart.keys():
              goods_info = shopping_cart[goods_name]
              print(f"name:{goods_name},price:{goods_info['price']},amount:{goods_info['amount']}")
        case"5":
            break
        case _ :
            print("wrong")



