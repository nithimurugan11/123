#functions with parameters
balance=[100000,50000,25000,10000]

def debit(money=0,pos=0):
    if money<=balance[pos]:
        balance[pos]-=money
        print(money,"debited")
        return balance[pos]
    else:print("not debited")

a=debit(1000,2)
print(a)
      
