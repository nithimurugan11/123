class choclate:
    def name(self):
        print("temptation")

class choclate1:
    def name1(self):
        print("dairy milk")

class choclate2(choclate,choclate1):
    def name2(self):
        print("blueberry")

a=choclate2()
a.name()
a.name1()
a.name2()



