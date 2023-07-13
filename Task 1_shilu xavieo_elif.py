#hotstar membership
days=int(input("enter the day"))
if days==0:
    print("good no fine")
elif days>=1 and days <=5:
    print("fine amount:","5 rs fine")
        
elif days >=5 and days <=10:
    print("fine amount:","10 rs fine")
elif days >=10 and days <=30:
    print("fine amount:","15 rs fine")
else:
    print("member ship cancelled")
