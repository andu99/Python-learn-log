print("hello".upper())

name = "andu"

print(name.startswith("and"))
print("meinv.png".endswith(".png"))
print("123".isdigit())
print("  andu  ".strip())
print("_".join(['武汉', '黄石', '黄冈']))  # 武汉_黄石_黄冈
print("andu_99".split("_"))  # ['andu', '99']
print(name.find("an"))  # 0
print(name.index("u"))  # 3
print(name.count("d"))  # 1
print(name.replace("u", "haha"))

"""
列表
列表转成字符串  join
字符串分割成列表  split
"""

cities = "北京 上海 重庆 武汉"
ret = cities.split(" ")
print(ret)  # ['北京', '上海', '重庆', '武汉']
ret2 = "_".join(ret)
print(ret2)  # 北京_上海_重庆_武汉
ret3 = "".join(ret)
print(ret3)  # 北京上海重庆武汉

"""
python 运算符
+ - * / %
> < >= <= == !=
= += -= *= /= %=
and
or
not
in
"""
experience = 10
experience += 20
print(experience)  # 30


