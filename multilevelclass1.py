class education:
    def twelth(self):
       print ("hr secondry school") 

class education1(education):
    def bcom(self):
        print ("under gradugate")

class education2(education1):
    def mcom(self):
        print ("post gradugate")

a=education2() 
a.twelth()
a.bcom()
a.mcom()

