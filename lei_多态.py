


class dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 在玩耍" % self.name)


class xiaotianquan(dog):
    def game(self):
        print("%s 游到海里去玩耍" % self.name)


class person(object):
    def __init__(self, name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s 正在和狗[%s] 在玩耍"
              %(self.name,dog.name))
        dog.game()

dog_obj = dog("旺财")
person_obj = person("xiaomei")
person_obj.game_with_dog(dog_obj)
print("***********多态 **************")
xiaotianquan_obj = xiaotianquan("哮天犬")
person_obj.game_with_dog(xiaotianquan_obj)