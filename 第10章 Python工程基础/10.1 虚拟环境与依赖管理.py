# 环境与依赖管理
# 核心目标是让项目能够在另一台电脑上复现。
# 项目代码
# + Python 版本
# + requirements.txt
# + 虚拟环境
# = 可复现运行环境

# - 每个项目使用独立虚拟环境；
# - requirements.txt 保存第三方依赖；
# - 标准库不需要写入依赖文件；
# - python -m pip 比直接使用 pip 更可靠；
# - .venv 通常不提交到 Git；
# - pip freeze 是当前环境快照，不一定等于项目真正需要的直接依赖。


