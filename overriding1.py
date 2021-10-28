#overriding is nothing but inheriting(like polymorphisim)
class python1:
    def fun(self):
        print("nithya")

class python2(python1):
    def fun(self):
        super().fun()
        print("aarthi")

class python3(python2):
    def fun(self):
        super().fun()
        print("anakilli")

a=python3() 
a.fun()       