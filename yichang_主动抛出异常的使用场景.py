# 异常类
#创建异常对象
#抛出异常

def input_password():
    # 1 提示输入密码
    word = input("请输入密码: ")
    # 2 判断密码长度 >= 6 输出密码
    if len(word) >= 6 :
        return print("*"*len(word))

    # 3 主动抛出异常
    print("主动抛出异常")
    # 3.1 创建异常对象
    ex = Exception("密码长度不够")
    # 3.2 主动抛出异常
    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)