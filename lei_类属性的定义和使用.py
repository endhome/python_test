class tool(object):

    #使用赋值语句定义类的属性 记录工具的数量
    count = 0   #类的属性
    def __init__(self, name):  #类定义的对象的属性name
        self.name = name

        # self.count += 1 初始化类的属性 不能加self
        #应该使用 类名.属性名
        tool.count += 1

print("现在工具的总数是:[%d]" %tool.count)
tool1 = tool("斧子")
print("现在工具的总数是:[%d]" %tool.count)
tool2 = tool("锤子")
print("不建议的方式---现在工具的总数是:[%d]" %tool2.count)
print("现在工具的总数是:[%d]" %tool.count)
tool3 = tool("追子")
print("现在工具的总数是:[%d]" %tool.count)
tool4 = tool("馆子")
print("现在工具的总数是:[%d]" %tool.count)
tool5 = tool("刀子")
print("现在工具的总数是:[%d]" %tool.count)
print("不建议的方式---现在工具的总数是:[%d]" %tool5.count)
print("不建议的方式---现在工具的总数是:[%d]" %tool2.count)
tool6 = tool("具子")
print("现在工具的总数是:[%d]" %tool.count)
print("不建议的方式---现在工具的总数是:[%d]" %tool6.count)

print("**************使用对象名+属性赋值语句会创建实例属性*****************")
tool6.count= 1000
print("tool6 现在工具的总数是:[%d]" %tool6.count)
print("现在工具的总数是:[%d]" %tool.count)