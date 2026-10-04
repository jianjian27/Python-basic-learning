# 异常边界的核心思想：
# 底层组件处理“怎么失败”，上层组件决定“如何向用户表达失败”。
#
# 不要让 SDK 的 AuthenticationError、TimeoutError 等细节泄漏到整个项目。
# 在服务边界把它们转换成项目自己的异常，调用者只依赖稳定的业务异常。


class PaperServiceError(RuntimeError):
    """论文服务调用失败。"""


def fetch_paper(paper_id: str, client) -> str:
    """调用外部服务获取论文摘要。"""
    if not paper_id.strip():
        raise ValueError("paper_id 不能为空")

    try:
        response = client.get_paper(paper_id)
    except TimeoutError as exc:
        # 保留原始异常链，同时向上层提供稳定的项目异常。
        raise PaperServiceError("论文服务请求超时") from exc
    except ConnectionError as exc:
        raise PaperServiceError("无法连接论文服务") from exc

    if not response:
        raise PaperServiceError("论文服务返回空结果")

    return response


class FakePaperClient:
    def __init__(self, result: str | None = "论文摘要"):
        self.result = result

    def get_paper(self, paper_id: str) -> str | None:
        return self.result


def main() -> None:
    client = FakePaperClient()

    try:
        summary = fetch_paper("paper-1", client)
    except PaperServiceError as exc:
        # 这一层负责决定如何提示用户或记录日志。
        print(f"获取论文失败：{exc}")
    else:
        print(f"获取成功：{summary}")


if __name__ == "__main__":
    main()
