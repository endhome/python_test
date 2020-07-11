"""
父类的方法不能满足子类的需求
在子类中重写父类中继承的方法
子类中有和父类同名的方法
子类对象在调用的时候默认调用的是子类中的方法
"""

class anamil:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

#继承动物类
class dog(anamil):
    def bark(self):
        print("汪汪叫...")


class xiaotianquan(dog):
    def fly(self):
        print("会飞的哮天犬")
    def bark(self):
        print("这是哮天犬在汪汪叫...")
        print("!@#$%^^&**((*&^%$$##")

        super().bark()  # 新版调用父类的方法

        """
        早期2.x 版本中子类对象调用父类方法
        父类名.父类的方法（子类的对象）
        不能使用子类名 否则会出现递归调用
        """
        anamil.drink(self)   #



dog1 = anamil()
dog1.eat()
dog1.drink()
dog1.run()
dog1.sleep()
print("********************************")
dog2 = dog()
dog2.eat()
dog2.drink()
dog2.run()
dog2.sleep()
dog2.bark()
print("********************************")
tianquan = xiaotianquan()
tianquan.drink()
tianquan.bark()
tianquan.fly()

"""
早期2.x 版本中子类对象调用父类方法
父类名.父类的方法（子类的对象）
"""