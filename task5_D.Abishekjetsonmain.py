#salery calculaction based on target achieved
basicpay=15000
name=input ("Enter the name:")
target=int(input("enter the value:"))
if(target<100000):
    print("the comission",name,(basicpay+(0.15*target)))
elif(target>=100000 and target<250000):
    print("the comission",name,(basicpay+(0.19*target)))
elif(target>250000):
    print("the comission",name,(basicpay+(0.22*target)))

