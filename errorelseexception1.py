#Else exception error
try:
    no=int(input("enter he value"))

except ValueError as e:
    print("value error",e)
else:
    print("value is",no)         
