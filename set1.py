a={'aa','bb','cc'}
print(a)
print(a)
print(a)

print(type(a))
print(len(a))
print(a)

#set constructor
c=set(('"mm','nn',1,2,3,4))
print(c)
c.add('xx')
print(c)
c1={"ss","xx"}
c.update(c1)
print(c)

#iteratable
d={"aa","bb","cc"}
d1=(1,2,3,4,5)
d.update(d1)
print(d)

x={"dd","ee",6,7,8}
x.remove(6)
x.discard("dd")
print(x)

#popmethod
s={"sam",4,5}
s1=s.pop()
print(s1)
