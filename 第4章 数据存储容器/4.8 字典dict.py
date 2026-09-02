# Python中的字典(dict)，里面存储的是键值对(key:value)类型的数据
# 可以根据键(key)找的对应的值(value)
# 键值对存储，键不能重复，可以修改，重复则后面的值会覆盖原有的值
# value可以是任何类型的数据，而key不能为可变类型，如不能为list，set，dict

dict1 = {"czr":624}
print(dict1["czr"])

dict1["czr"] = 520
print(dict1["czr"])