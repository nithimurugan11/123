class oper:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
object=oper(10,20)   

class operator:
    def __init__(self,a):
        self.a=a
        print(self.a+self.a)
object1=operator(10)
object2=operator(20)
print(object1.a+object2.a)

class opera:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        self.b=b
        return self.a+b.a
ob=opera(20) 
ob1=opera(50)        
print("sum",ob+ob1)