
#Fine amount for membership problem

day=int(input("Enter the number of days after your plan was expired:"))
amount=299

if day==0:
    print("You have no fine.Amount to be paid is",amount)
elif (day>=1 and day<5):
    print("You have fine of 5.The amount should be paid is ",amount*5,".rs")
elif (day>=5 and day<10):
    print("You have fine of 10.The amount should be paid is ",amount*10,".rs")
elif (day>=10 and day<30):
    print("You have fine of 15.The amount should be paid is ",amount*15,".rs")
else:
    print("Your membership was cancelled ")


