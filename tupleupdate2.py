a=('aa','bb','cc','dd','ee')
b=list(a) 
b[3]='bc'
a=tuple(b)
print(a)
 
x=('one','two','three')
y=list(x)
y.append('three')
x=tuple(y)
print(x)

m=('one','two','three')
n=('four',)
m+=n
print(m)

c=('aa','bb','cc')
d=list(c)
d.remove('aa')
c=tuple(d)
print(c)
c.clear() #can't be clear
print(c)




