# Mock 的意义：在测试中用“假的外部服务”替代真实 API。
#
# 为什么需要 Mock？
# - 测试不依赖网络；
# - 不消耗真实模型额度；
# - 结果稳定、执行快速；
# - 可以主动模拟超时、认证失败等异常。
#
# 本例使用依赖注入：ask_model() 不在函数内部创建 OpenAI 客户端，
# 而是由调用者传入 client。这样测试时可以传入 Mock。

import unittest
from types import SimpleNamespace
from unittest.mock import Mock


def ask_model(prompt: str, client) -> str:
    """调用外部模型，并返回模型文本。"""
    response = client.chat.completions.create(
        model="demo-model",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


class AskModelTests(unittest.TestCase):
    def test_returns_model_content_without_real_network_request(self):
        # Arrange：准备一个假的客户端和假的 API 响应。
        client = Mock()
        client.chat.completions.create.return_value = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="模型回答")
                )
            ]
        )

        # Act：调用真正要测试的业务函数。
        result = ask_model("什么是同步控制？", client)

        # Assert：验证业务结果和外部调用行为。
        self.assertEqual(result, "模型回答")
        client.chat.completions.create.assert_called_once()

    def test_can_simulate_timeout(self):
        client = Mock()
        client.chat.completions.create.side_effect = TimeoutError(
            "模拟请求超时"
        )

        with self.assertRaises(TimeoutError):
            ask_model("测试问题", client)


if __name__ == "__main__":
    unittest.main(verbosity=2)
