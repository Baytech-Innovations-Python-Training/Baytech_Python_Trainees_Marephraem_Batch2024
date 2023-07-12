#Task 1
#calculating the fine
days=int(input("enter the number of days:"))
if days<=0:
    print("good no fine")
elif days>=1 and days<=5:
    print("fine amount:5")
elif days>=5 and days<=10:
    print("fine amount:10")
elif days>=10 and days<=30:
    print("fine amount:15")
else:
    print("membership cancel")
