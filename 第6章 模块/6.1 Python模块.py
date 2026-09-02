# Python模块(module):一个.py文件就是一个模块，模块是Python程序的基本组织单位。在模块中可以定义变量，函数，类，以及可执行的代码
# 自定义模块，内置模块

# 导入模块
# 在使用模块中提供的功能之前，必须先导入，再使用
# import 模块名
# import 模块名 as 别名
# from 模块名 import 功能名
# from 模块名 import 功能名 as 别名
# from 模块名 import *

# import random
#
# for i in range(10):
#     print(random.randint(1,100))
#
# import random as rd
# for i in range(10):
#     print(rd.randint(1,100))

# from random import randint
# for i in range(10):
#     print(randint(0,100))

from random import * #导入一个模块内的所有功能
for i in range(10):
    print(randint(0,100))

# 自定义模块
# __name__
# __all__