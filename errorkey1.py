# Key error
try:
    a={"name":"nithya","name1":"aarthi"}
    print(a['age'])

except KeyError as e:
    print("key error:",e)
    