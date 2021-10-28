'''err=dir(locals()['__builtins__'])
print(err)
print(len(err))'''

#Zero division error
try:
    a=10
    b=2
    c=a/b
    print(c)
except Exception as e:
    print(e)