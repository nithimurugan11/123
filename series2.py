count=0
previous=0
for i in range(10):
    amount=int(input("current balance="))
    if amount>previous:
        count+=1
    previous=amount
print(count)