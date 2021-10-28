#Value error
try:
    no=int(input("Enter the value"))
    print(no)

except ValueError as e:
    print("value error",e)
