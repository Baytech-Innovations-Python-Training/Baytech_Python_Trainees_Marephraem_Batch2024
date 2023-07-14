#based on the commision it will calculate salary
Name=input("Enter the name:")
Basicpay=15000
Target=int(input("Enter the value:"))
if(Target<100000):
    commision=Target*(15/100)
    print("commision:",commision)
elif(Target>=100000 and Target<250000):
    commision=Target*(19/100)
    print("commision:",commision)
elif(Target>250000):
    commision=Target*(22/100)
    print("commision:",commision)
salary=Basicpay+commision
print("Name:",Name)
print("Salary:",salary)
