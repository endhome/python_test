"""
私有
__方法名
__属性名
"""

class A:
    def __init__(self):
        # 共有属性
        self.num1 = 100
        # 私有属性
        self.__num2 = 200

    #私有方法
    def __test(slef):
        print("A的私有方法")
        print("私用方法：%d --- %d"%(slef.num1,slef.__num2))

    def pub_test(self):
        print("A的public方法")

    def the_public_way_access_private_shuxing_offer_to_sub_class(self):
        print("父类共有方法访问自己类的私有属性，从而提供给子类访问父类私有属性和方法的方式")
        print("父类共有方法访问自己类的私有属性 【%d】" % self.__num2)


class B(A):
    def  demo(self):
        # 不能访问父类的私有属性和私有方法
        # print("子类访问父类的私有属性会出错 %d" % self.__num2)
        # A.__test()

        #可以访问子类的非私有方法和属性
        print("子类访问父类的共有属性 %d" % self.num1)

        A.pub_test(self)  #括号必须要加self 调用方式:父类名.父类方法(子类对象)
        A.the_public_way_access_private_shuxing_offer_to_sub_class(self)

#创建子类对象
b = B()
print(b)
print(b.num1)
#  print(b.__num2)  外界不能访问  私有
#b.__test()         外界不能访问  私有
b.pub_test()
b.demo()
print("**************************")
