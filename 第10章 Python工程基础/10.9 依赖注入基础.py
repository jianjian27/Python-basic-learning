# 依赖注入的核心思想：
# 函数需要什么，就从外部传入什么，不要在内部偷偷创建。
#
# 不推荐：
# def answer_question(question):
#     client = OpenAI(...)
#     retriever = Retriever(...)
# 更推荐：
# def answer_question(
#     question,
#     client,
#     retriever,
# ):
#     ...
# 这样做的好处：
# - 更容易测试；
# - 可以替换真实客户端；
# - 可以使用 Mock；
# - 减少全局变量；
# - 组件之间耦合更低。