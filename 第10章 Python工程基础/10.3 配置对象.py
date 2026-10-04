# 配置对象
# 当配置项很多时，使用对象管理配置项更方便。不需要到处调用 os.getenv()，只需要在配置对象中调用一次即可。
# 集中成一个配置对象
# @dataclass(frozen=True)
# class Settings:
#     api_key: str
#     base_url: str
#     model: str
#     timeout: float
#     max_tokens: int