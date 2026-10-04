"""pathlib 的可运行示例。

为什么要单独导入 ``Path``？
文件路径不是普通文本。手动使用字符串拼接时，需要自己处理 Windows 的
反斜杠、Linux 的斜杠、重复斜杠和父目录是否存在，代码容易出错。

``Path`` 把路径表示成对象，并提供 exists、mkdir、read_text、glob 等操作，
因此可以用同一套跨平台接口管理论文 PDF、数据库、缓存和日志目录。

本文件使用临时目录演示文件操作，程序结束后临时目录会自动删除，
不会修改真实项目文件。
"""

from pathlib import Path
from tempfile import TemporaryDirectory


def prepare_demo_files(base_dir: Path) -> tuple[Path, Path]:
    """创建一个论文目录和一个文本文件。

    ``parents=True`` 解决父目录不存在的问题，``exist_ok=True`` 让重复运行
    示例时不会因为目录已经存在而失败。
    """
    papers_dir = base_dir / "data" / "papers"
    papers_dir.mkdir(parents=True, exist_ok=True)

    text_path = papers_dir / "paper-notes.txt"
    text_path.write_text(
        "论文标题：非线性系统\n",
        encoding="utf-8",
    )

    pdf_path = papers_dir / "paper-demo.pdf"
    pdf_path.write_bytes(b"fake pdf bytes")

    return text_path, pdf_path


def inspect_directory(base_dir: Path) -> None:
    """展示常见的路径属性和文件搜索操作。

    这些方法让业务代码不必自己拆分文件名、判断后缀或遍历目录字符串。
    ``read_text`` 用于文本，``read_bytes`` 用于 PDF 等二进制文件。
    """
    papers_dir = base_dir / "data" / "papers"

    print("目录存在：", papers_dir.exists())
    print("目录是文件夹：", papers_dir.is_dir())

    for item in papers_dir.iterdir():
        print(
            "名称=",
            item.name,
            "后缀=",
            item.suffix,
            "是否文件=",
            item.is_file(),
        )

    pdf_files = list(papers_dir.glob("*.pdf"))
    print("找到的 PDF：", pdf_files)


if __name__ == "__main__":
    with TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        text_path, pdf_path = prepare_demo_files(base_dir)

        print("文本文件：", text_path)
        print("文件名：", text_path.name)
        print("文件主名：", text_path.stem)
        print("文件后缀：", text_path.suffix)
        print("父目录：", text_path.parent)

        print(
            "文本内容：",
            text_path.read_text(encoding="utf-8").strip(),
        )
        print("PDF 字节：", pdf_path.read_bytes())

        inspect_directory(base_dir)
