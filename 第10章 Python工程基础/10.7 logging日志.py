"""logging 的最小工程化示例。

为什么需要 logging？
如果只使用 print()，当程序变大后，很难知道消息来自哪个模块、发生在
什么时间、属于正常信息还是错误，也很难统一关闭调试输出或改写到文件。

logging 提供了统一的时间、级别、来源和输出方式。print() 适合临时观察
一个值；logging 适合长期运行的项目，例如记录 PDF 解析进度、Chunk 数量、
模型请求耗时和异常堆栈。
"""

import logging
import time


def configure_logging(level: int = logging.INFO) -> logging.Logger:
    """在应用入口配置一次日志，并返回本模块使用的 logger。

    单独配置入口的好处是：所有模块遵守同一格式，避免每个模块重复配置
    handler，导致同一条日志被打印多次。
    """
    logger = logging.getLogger("paper_learning")

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )
        )
        logger.addHandler(handler)
        logger.propagate = False

    logger.setLevel(level)
    return logger


logger = logging.getLogger("paper_learning")


def build_chunks_demo(chunk_count: int) -> int:
    """模拟 Chunk 构建过程，展示不同级别日志的使用场景。"""
    if chunk_count < 0:
        logger.error("Chunk 数量不能为负数：%d", chunk_count)
        raise ValueError("chunk_count 不能小于 0")

    logger.info("开始构建 Chunk，预计数量：%d", chunk_count)
    start = time.perf_counter()

    if chunk_count == 0:
        logger.warning("没有需要构建的 Chunk")

    time.sleep(0.01)
    elapsed = time.perf_counter() - start
    logger.info(
        "Chunk 构建完成，数量：%d，耗时：%.3f 秒",
        chunk_count,
        elapsed,
    )
    return chunk_count


def run_with_error_log() -> None:
    """展示 logger.exception() 会记录异常堆栈。

    只写 logger.error("出错") 会丢失 traceback；exception() 能保留定位问题
    所需的调用栈，但仍然不应把 API Key 或论文全文写入日志。
    """
    try:
        int("不是数字")
    except ValueError:
        logger.exception("解析配置失败")


if __name__ == "__main__":
    configure_logging(logging.DEBUG)

    logger.debug("这是调试细节")
    build_chunks_demo(3)
    build_chunks_demo(0)
    run_with_error_log()
