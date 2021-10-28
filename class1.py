class a:
    name="raja"  
    def __init__(self,nith):
            self.nith=nith
obj1=a("good")  
obj2=a("bad") 
print("play is boy {}".format(obj1.__class__.name))
print("play is boy {}".format(obj2.__class__.name))
print("car is {}".format(obj1.nith))
print("name is {}".format(obj2.nith))