# 模块是一个 .py 文件，包是组织多个模块的目录。
# 例如：项目结构：
# domain/
# ingestion/
# utils/
# models/
# tests/

# 基本原则：
# domain：数据模型
# ingestion：数据导入和转换
# utils：通用工具
# models：外部服务
# tests：测试

# 要避免domain 导入 ingestion，ingestion 又导入 domain，产生循环导入
# 绝对导入：从项目的根目录开始导入模块
# 相对导入：从当前模块所在的包开始导入模块
# 依赖方向：从低级模块向高级模块导入，避免反向依赖
# 绝对导入示例：
# from domain import user
# 相对导入示例：
# from . import user
