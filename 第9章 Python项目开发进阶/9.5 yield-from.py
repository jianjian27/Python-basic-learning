# yield from 当前生成器暂时把产生元素的工作交给另一个可迭代对象
# 假设一个子生成器
def child_generator():
    yield "Child 1"
    yield "Child 2"
# 如果外层生成器想把这些元素继续提供出去，可以手动写
def parent_generator():
    for value in child_generator():
        yield value

# 但是，使用 yield from 可以更简洁地实现相同的功能
def parent_generator_v2():
    yield from child_generator()

# yield child() 交出子生成器对象
# yield from child() 交出子生成器产生的所有值

# 起到一种 “委托 ” 的作用，父生成器把 “如何继续产生下一项数据 ”的工作，暂时交给子生成器负责
def child():
    yield "A"
    yield "B"

def parent():
    yield from child()
    yield "C"
# 调用
print(list(parent())) # 输出: ['A', 'B', 'C']，父生成器先委托给子生成器产生'A'和'B'，然后继续产生'C'。
# 在 yield from child() 执行期间，父生成器暂停，子生成器接管控制权，直到子生成器耗尽所有值。然后父生成器恢复执行，继续产生'C'。
# 如果不使用 yield from ,父生成器需要自己管理
def parent_manual():
    for value in child():
        yield value
    yield "C" # 父生成器必须调用子生成器，逐个获取子生成器的值，再逐个 yield 出去，代码更冗长。