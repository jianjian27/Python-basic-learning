# 递归携带上下文
def walk_titles(
        chapters: list[dict],
        parent_path: tuple[str, ...] = (),
):
    for chapter in chapters:
        current_path = (
            *parent_path,
            chapter["title"],
        )

        yield current_path
        yield from walk_titles(
            chapter["children"],
            current_path,
        )

chapters = [
        {
            "title": "第1章",
            "children": [
                {
                    "title": "1.1 背景",
                    "children": [],
                },
                {
                    "title": "1.2 模型",
                    "children": [
                        {
                            "title": "1.2.1 方程",
                            "children": [],
                        }
                    ],
                },
            ],
        }
    ]



for path in walk_titles(chapters):
    print(" > ".join(path))