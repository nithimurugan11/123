class family:
    def name(self):
        print("father")
class m(family):
    def name1(self):
        print("mother")
class n(family):
    def name2(self):
        print("child1")
class o(family):
    def name3(self):
        print("child2")
x=m()
y=n()
z=o()

x.name()
x.name1()
y.name2() 
z.name3()        
