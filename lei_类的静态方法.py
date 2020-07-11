

"""
如果一个类中有一个方法
这个方法既不需要访问实例属性或者实例的方法
也不需要访问类的属性或者调用类的方法
则可以考略将该方法封装成一个 静态的方法

不需要创建对象就可以调用静态方法

静态方法的调用     格式： 类名.静态方法名
类方法的调用       格式： 类名.类对象方法
类属性的调用       格式： 类名.类属性名
类属性初始化方法   格式： 类名.类属性名 = value

"""


class dog(object):

    count = 1

#静态方法 不需要self参数
    @staticmethod
    def run():
        print("dog is running .....")

#类方法
    @classmethod
    def print_count(cls):
        print("now the dog total is [%d]" % cls.count)

    def __init__(self, name):
        self.name = name
        dog.count += 1



dog.run()
#dog.print_count()
print("***************************")
dog1 = dog("旺财")
dog.run()
dog.print_count()