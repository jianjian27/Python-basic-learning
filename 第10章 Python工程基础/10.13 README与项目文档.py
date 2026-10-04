# README 是项目给“第一次接触项目的人”看的使用说明。
#
# 它不是随便写的介绍，而是项目的使用接口，至少应回答：
# 1. 项目解决什么问题？
# 2. 如何安装依赖？
# 3. 如何配置环境变量？
# 4. 如何运行程序？
# 5. 如何运行测试？
# 6. 当前完成了什么、限制是什么？
#
# 文档和代码一样需要持续维护：代码入口、命令或环境变量变化时，README
# 也要同步更新，否则别人无法复现项目。

REQUIRED_README_SECTIONS = (
    "项目简介",
    "环境要求",
    "安装",
    "配置",
    "运行",
    "测试",
    "项目结构",
    "当前限制",
)


def missing_sections(readme_text: str) -> list[str]:
    """返回 README 中缺少的最低限度章节。"""
    return [
        section
        for section in REQUIRED_README_SECTIONS
        if section not in readme_text
    ]


README_TEMPLATE = """# 项目名称

## 项目简介
说明项目解决的问题和主要功能。

## 环境要求
- Python 3.10+

## 安装
```powershell
python -m venv .venv
python -m pip install -r requirements.txt
```

## 配置
复制 `.env.example` 为 `.env`，填写本地配置；不要提交真实密钥。

## 运行
说明启动命令和访问方式。

## 测试
```powershell
python -m unittest discover -s tests -v
```

## 项目结构
说明主要目录的职责。

## 当前限制
记录尚未实现的功能和已知问题。
"""


if __name__ == "__main__":
    missing = missing_sections(README_TEMPLATE)
    print("缺少的 README 章节：", missing or "无")
