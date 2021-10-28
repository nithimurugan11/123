name=[]
mark=[]
for i in range(3):
    a=input("enter the name")
    b=int(input("enter the mark"))
    name.append(a)
    mark.append(b)
h=max(mark)
l=min(mark)
print(h)
print(l) 
for i in range(5):
    if h==mark[i]:
        print("h:",name[i])
    if l==mark[i]:
        print("l:",name[i])  






