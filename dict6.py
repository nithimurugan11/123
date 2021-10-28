a={"name":"nithya","age":"21","college":"ksr","frnd":"keerthi"}
print(a)
b=a.copy()
print(b)

b=dict(a)
print(b)

b=a.setdefault("name") #or ("name","nithya")
print(b)

