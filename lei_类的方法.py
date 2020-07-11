
class  tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        tool.count += 1

    # 表示类的方法
    @classmethod
    def show_to_count(cls):
        print("工具对象的总数是[%d]" % cls.count)

tool1 = tool("斧子")
print("现在工具的总数是:[%d]" %tool.count)
tool.show_to_count()
tool2 = tool("锤子")
tool3 = tool("追子")
tool4 = tool("馆子")
print("现在工具的总数是:[%d]" %tool.count)
tool.show_to_count()