class father:
    def __init__(self):
        pass

    def father_demo(self):
        print("father demo")

    def address(self):
        print("上海陆家嘴")


    def __del__(self):
        print("father del....")


class mother:
    def __init__(self):
        pass

    def mother_demo(self):
        print("mother demo")

    def address(self):
        print("上海陆家嘴.......")

    def __del__(self):
        print("mother del....")


# 多继承
class child(father, mother):
    def demo(self):
        print("child demo")

        #必须写参数self
        father.address(self)
        mother.address(self)

    def __del__(self):
        print("child del....")


child_obj = child()
child_obj.father_demo()
child_obj.mother_demo()
child_obj.demo()

#存在同名的方法的时候 默认调用的是第一个继承类的方法 class child(father, mother):
child_obj.address()

# 查看子类调用父类方法的顺序 class child(father, mother)
print(child.__mro__)
print("******************************")
print(dir(child_obj))
