"""
异常的传递性的处理 eg

def demo1():
    return int(input("请输入一个数： "))
def demo2():
    return demo1()
print(demo2())


请输入一个数： e
Traceback (most recent call last):
  File "H:/lei/yichang_异常的传递性.py", line 8, in <module>
    print(demo2())
  File "H:/lei/yichang_异常的传递性.py", line 6, in demo2
    return demo1()
  File "H:/lei/yichang_异常的传递性.py", line 3, in demo1
    return int(input("请输入一个数： "))
ValueError: invalid literal for int() with base 10: 'e'

"""



def demo1():
    return int(input("请输入一个数： "))

def demo2():
    return demo1()

try:
    print(demo2())
except Exception as result:
    print("出现了错误: [%s]" % result)
