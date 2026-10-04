# 环境变量与.env
# 配置与代码分离，密钥与代码分离
# 代码中不写：API_KEY = "真实密钥"
# 代码中写：API_KEY = os.getenv("API_KEY")

# 环境变量读取出来都是字符串；
# int、float、bool 必须手动转换；
