class A:
    def aa(self,a):
        print(a)
    def aa(self,a,b):
        print(a+b)  
    def aa(self,a,b,c):
        print(a+b+c)  
a=A()
a.aa(10) 

class sum:
    def a(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return (a+b+c)
        elif a!=None and b!=None:
            return (a+b)
        else:
            return(a)  

x=sum()
print("sum",x.a(10,20,30))   
print("sum",x.a(20,30))  
print("sum",x.a(50)) 

