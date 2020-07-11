class father:
    def __init__(self):
        pass
    def father_demo(self):
        print("father demo")
    def __del__(self):
        print("father del....")


class mother:
    def __init__(self):
        pass
    def mother_demo(self):
        print("mother demo")

    
    def __del__(self):
        print("mother del....")

#多继承
class child(father, mother):
    def demo(self):
        print("child demo")
    def __del__(self):
        print("child del....")



child_obj = child()
child_obj.father_demo()
child_obj.mother_demo()
child_obj.demo()