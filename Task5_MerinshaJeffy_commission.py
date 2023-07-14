#finding the target
name=input("enter thhe employee name:")
target=int(input("enter the target"))
basicpay=15000
a=(target*0.15)
b=(target*0.19)
c=(target*0.22)
if target>100000:
    commission  =a
elif target<=100000>250000:
    commission =b
    
elif target<250000:
     commission =c
else:
    print("The condition is invalid")
grosspay=(basicpay  + commission)
print("the grosspay of",name,grosspay)
