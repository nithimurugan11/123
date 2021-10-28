a={"name":"kv","age":"21","game":"cricket"}
print(a)
print(a["age"])
b=a["name"]
print(b)
b=a.get("game")
print(b)
b=a.keys()
print(b)
b=a.values()
print(b)
a["food"]="biriyani"
print(a)


