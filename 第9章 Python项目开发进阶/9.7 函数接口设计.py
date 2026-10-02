# 函数接口就是其他代码调用这个函数时，需要知道的输入，输出和规则
# 一个好的函数接口应该让调用者清楚：
# 需要传入什么；
# 哪些参数必填；
# 哪些参数有默认值；
# 哪些参数必须使用关键字；
# 输入不合法时会发生什么；
# 返回什么类型；
# 内部复杂逻辑是否被隐藏。

# def build_chunks(
#         root_sections: list[Section],
#         paper_id: str,
#         *,
#         max_chars: int = 3000,
#         overlap_chars: int = 300,
# ) -> list[Chunk]:

# 前两个参数是必填位置参数，“ * ”之后的参数是关键字参数，调用时必须使用关键字传入，同时有默认值，调用者可以选择不传入，使用默认值即可。

"""Build traceable chunks from each section's direct text blocks.

    Children are traversed separately. This is important because ``Section.full_text``
    already contains child content and would otherwise duplicate evidence.
    """
# 文档字符串解释业务规则，不仅说明函数的功能，还说明了为什么要这样做，帮助调用者理解函数的设计意图。

    # if not paper_id.strip():
    #     raise ValueError("paper_id 不能为空。")
    # if max_chars <= 0:
    #     raise ValueError("max_chars 必须大于 0。")
    # if overlap_chars < 0:
    #     raise ValueError("overlap_chars 不能小于 0。")
    # if overlap_chars >= max_chars:
    #     raise ValueError("overlap_chars 必须小于 max_chars。")
    #

# 尽早校验输入，函数一开始就检查参数，避免错误配置进入后续复杂逻辑。如果没有这些校验，错误可能在函数内部很深的位置才暴露出来，调用者很难定位原因。

    # chunks = []
    # chunk_index = 0
    #

# 主函数不实现所有细节，而是协调调用其他函数完成任务。主函数的逻辑清晰，易于理解，复杂的细节被封装在其他函数中。
# 辅助函数采用下划线开头，表示它们是内部使用的，不是公共接口的一部分。这样可以让调用者知道哪些函数是可以直接使用的，哪些是内部实现细节。

    # for section, section_path in iter_sections_with_paths(root_sections):
    #     units = [
    #         unit
    #         for block in section.blocks
    #         for unit in _block_to_units(block, max_chars)
    #     ]
    #     current_units: list[_TextUnit] = []
    #
    #     for unit in units:
    #         candidate = [*current_units, unit]
    #
    #         if current_units and _content_length(candidate) > max_chars:
    #             chunks.append(
    #                 _make_chunk(
    #                     paper_id=paper_id,
    #                     chunk_index=chunk_index,
    #                     section_title=section.title,
    #                     section_path=section_path,
    #                     units=current_units,
    #                 )
    #             )
    #
    #             chunk_index += 1
    #             current_units = _select_overlap(
    #                 current_units,
    #                 overlap_chars,
    #             )
    #
    #             if (
    #                 current_units
    #                 and _content_length([*current_units, unit])
    #                 > max_chars
    #             ):
    #                 current_units = []
    #
    #         current_units.append(unit)
    #
    #     if current_units:
    #         chunks.append(
    #             _make_chunk(
    #                 paper_id=paper_id,
    #                 chunk_index=chunk_index,
    #                 section_title=section.title,
    #                 section_path=section_path,
    #                 units=current_units,
    #             )
    #         )
    #         chunk_index += 1
    #
    # return chunks

def search_chunks(
        query: str,
        chunks: list[str],
        *,
        top_k: int = 5,
) -> list[str]:
    if not query.strip():
        raise ValueError("query 不能为空。")
    if top_k <= 0:
        raise ValueError("top_k 必须大于 0。")
    if top_k > len(chunks):
        raise ValueError("top_k 不能大于 chunks 的长度。")

    return chunks[:top_k]

print(search_chunks(
    "同步控制",
    ["chunk A", "chunk B", "chunk C"],
    top_k=2,
))
