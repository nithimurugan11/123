class a:
    def name(self):
        print("parent class")
class b(a):
    def name1(self):
        print("child class") 
x=b()   
x.name()
x.name1()
            
