#Index error
try:
    a=[10,20,30,40]
    print(a[4])
except IndexError as e:
    print("Index error",e)

