"""
数据运算完成后，就会被python垃圾回收器回收。数据的开销对资源消耗较大，所以把常用的数据用变量来表示，减小系统开销。
"""
x = 1
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)

"""
变量变更指向的值，原值则会被回收，空间被释放
"""

'''
变量名：只能是小写、下划线和数字，数字不能开头，非 ASCII 字符 
'''
你好 = 11
print(你好)
my_first_name = '张'
mySecondName = '全蛋'

"""
基本数据类型：整型和浮点型
            布尔类型
            字符串类型
类型是人们抽象出来的一个概念
"""
print(bool(""))
# 但凡有字符，为真

"""
字符窜：转义
       格式化
       \n   换行
"""

age = 20
print("我的姓名是%s,年龄是%d。" % (my_first_name + mySecondName, age))
print(f"我的姓名是{my_first_name + mySecondName},年龄是{age}。")

"""
字符串有正索引，还有负索引
"""
str1 = "hello world"
print(str1[3])
print(str1[-1])

print("*" * 10)
"""
字符，字节，中文一个字符，2个字节
针对容器类型
len()
in 判断
"""
print("hello" in str1)

"""
input()阻塞函数
"""
# name = input("请输入姓名：")
# print(f"姓名：{name}")

print(True)
print(100, str1, sep=",")
