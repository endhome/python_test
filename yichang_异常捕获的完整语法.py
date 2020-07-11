
try:
    #不能确定正确执行的代码
    num = int(input("请输入一个整数:"))
    res = 8 / num
    print(" 8 / %d = %.2f" % (num,res))
except ValueError:
    #异常一
    print("输入的数字必须是整数")
except ZeroDivisionError:
    #异常二
    print("除数不能为0")
except Exception as result:
    #没有枚举出来的异常
    print("其他没有捕获到的异常将执行此处代码[%s]" %result)
else:
    #没有出现异常将要执行的代码
    print("正常运行，没有捕获到异常或者错误")
finally:
    #无论是否有异常 都会执行的代码
    print("不管是否有异常或者成功都会执行的代码")




