# unittest自动化测试
# 输入符合预期时，结果是否正确
# 边界条件下，程序是否安全
# 错误输入时，是否抛出正确异常
# 修改代码后，旧功能是否仍然正常

# 单元测试
# 单元测试验证一个相对独立的功能单元：
# 输入 → 函数 → 输出
# 例如：
# build_chunks(...)
# 可以测试：
# 给定章节和文本块
# → 是否生成正确的 Chunk
# 集成测试则验证多个组件是否能一起工作，例如：
# PDF 文件
# → PDF 解析
# → 章节识别
# → Chunk 构建
# → 数据库存储

# 一个测试通常采用：Arrange：准备数据， Act：调用被测试代码， Assert：验证结果
# def test_ids_are_deterministic(self):
#     section = Section(
#         title="结论",
#         level=1,
#         blocks=[make_block(7, 1, "研究结论")],
#     )
#
#     first = build_chunks([section], "paper-4")
#     second = build_chunks([section], "paper-4")
#
#     self.assertEqual(first[0].id, second[0].id)
#     self.assertEqual(first[0].content_hash, second[0].content_hash)

# unittest 是 Python 内置的单元测试框架，使用它可以方便地编写和运行测试用例。
# unittest 的基本使用方法如下：
# 1. 导入 unittest 模块
# import unittest
# 2. 创建一个测试类，继承 unittest.TestCase
# class ChunkBuilderTests(unittest.TestCase):
# 3. 所有测试方法必须以 test_ 开头
#     def test_ids_are_deterministic(self):

# 4. 使用 self.assertEqual()判断两个值相等、self.assertTrue()判断结果为真、self.assertFalse()判断结果为假、assertLessEqual
# 判断左边小于或等于右边、assertIn()判断元素是否存在、assertIsNone()判断结果是 None 等方法进行断言

# 测试异常
# 使用 self.assertRaises() 方法来测试代码是否会抛出指定的异常
# 例如：
# def test_invalid_input_raises_exception(self):
#     with self.assertRaises(ValueError):
#         build_chunks([section], "invalid_input")

# 测试辅助函数
# 可以在测试类中定义辅助函数来简化测试代码，例如：
# def make_block(page: int, block_id: int, text: str) -> TextBlock:
# 辅助函数把测试数据构造集中起来

# 5. 运行测试
# 可以在命令行中运行测试文件：python -m unittest discover -s tests -v
# python -m unittest
# → 使用 unittest 模块运行
#
# discover
# → 自动发现测试
#
# -s tests
# → 从 tests 目录开始查找
#
# -v
# → 显示详细测试名称

# 6. 测试结果
# 测试结果会显示每个测试用例的执行情况，包括成功、失败
# 成功的测试用例会显示为 .
# 失败的测试用例会显示为 FAIL或者 ERROR ，FAIL：代码运行了，但断言结果不符合预期，ERROR：测试执行过程中发生了未预期异常