count=0
for ticket in range(3):
    amount=int(input("amount="))
    if(amount>=500):
        print("ticket booked")
else:
        print("insufficient amount")    
        count+=1
print('count',count)

