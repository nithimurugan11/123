class A:
    def __init__(self):
        print("hai")

    def b(self):
        print("hello") 
a=A() #to call only constractor
a.b() #to call const with function

class B: #constractor with parameter
    def __init__(self,name,age,college):
        print("name:",name)
        print("age:",age)
        print("college:",college)
b=B("nithi","21","ksr")  

class C:
    def __init__(self,sub,batch):
        self.s=sub
        self.b=batch

    def fun(self):
        print("sub:",self.s)
        print("batch:",self.b) 
c=C("maths","second")  
c.fun()         