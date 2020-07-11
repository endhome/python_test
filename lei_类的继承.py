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

class cat(anamil):
    def catch(self):
        print("抓老鼠的猫")

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
print("********************************")
catt = cat()
catt.drink()
catt.catch()