"""
数据运算完成后，就会被python垃圾回收器回收。数据的开销对资源消耗较大，所以把常用的数据用变量来表示，减小系统开销。
"""
x = 1
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
