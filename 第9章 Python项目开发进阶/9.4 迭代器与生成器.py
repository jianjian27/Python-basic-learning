# 可迭代对象负责 “可以被遍历 ”，迭代器负责 “记住当前遍历到哪里 ”

# 列表是可迭代对象，它可以被for遍历
numbers = [10, 20, 30]
for number in numbers:
    print(number)

# 也可以通过 iter() 函数将可迭代对象转换为迭代器
iterator = iter(numbers)
# 使用next()逐个取值
print(next(iterator))  # 输出: 10
print(next(iterator))  # 输出: 20
print(next(iterator))  # 输出: 30
# 如果继续调用next()，会引发StopIteration异常

# for循环实际上帮我们处理了iter()、next()、StopIteration

# 生成器表达式也是迭代器
squares = (number * number for number in range(3))

print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4
print(list(squares))  # 输出: []，因为生成器已经被耗尽,消费完后不能自动重置

# 生成器函数与yield
# 包含yield的函数叫生成器函数
def count_up_to(limit: int):
    number = 1
    while number < limit:
        yield number
        number += 1

# 调用生成器函数不会立即执行函数体，而是返回一个生成器对象
counter = count_up_to(5)
print(counter) # 输出<generator object count_up_to at 0x...>
# 只有调用next()时，生成器函数才会执行，直到遇到yield语句暂停，并返回yield后的值
print(next(counter))  # 输出: 1
print(next(counter))  # 输出: 2
print(next(counter))  # 输出: 3
# 每次遇到yield，生成器函数会暂停，并记住当前的执行状态。下一次调用next()时，会从上次暂停的地方继续执行。
# 普通 return 会直接结束函数

for number in count_up_to(7):
    print(number)  # 输出: 1, 2, 3, 4, 5, 6

# 生成器中的 return 语句会引发StopIteration异常，并且可以携带一个返回值。这个返回值可以通过捕获StopIteration异常来获取。
def example():
    yield 1
    return "遍历结束"
    yield 2 # yield 2永远不会被执行，因为 return 已经结束了函数

generator = example()
print(next(generator))  # 输出: 1
# 可以手动捕获StopIteration异常并获取返回值
try:
    print(next(generator))
except StopIteration as e:
    print(f"StopIteration: {e}")
# 普通 for 循环会自动处理 StopIteration 异常，所以不会显示返回值
for value in example():
    print(value) # 只会输出 1

# yield 是 “交出一个结果，稍后继续 ”，return 是 “结束整个生成过程 ”