try:
    #不能确定正确执行的代码
    num = int(input("请输入一个整数:"))
    res = 8 / num
    print(" 8 / %d = %.2f" % (num,res))
except ValueError:
    print("输入的数字必须是整数")
#except ZeroDivisionError:
#    print("除数不能为0")
#print("----------------------------")

#捕获未知的错误类型
except Exception as result:
    print("未知错误 %s" % result)


