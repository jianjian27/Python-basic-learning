# 异常：在程序执行过程中发生的错误，会导致程序的正常流程被中断。
# 不做处理：直接让异常抛出，程序会因为异常而终止。
# 捕获异常：使用try-except语句捕获异常，程序不会终止，而是执行except块中的代码。

try:
    # 可能出错的代码
    pass

except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

except Exception as e:
    print(e)

else:
    # 没有发生异常时执行
    print("程序正常结束")

finally:
    # 无论是否发生异常都会执行
    print("释放资源")