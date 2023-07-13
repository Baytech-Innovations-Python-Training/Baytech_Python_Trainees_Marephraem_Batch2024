#Salary calculation
#based on commission
name=input("Enter the employee name:")
basicpay=15000
target=int(input("Enter the Target Achieved:"))
if target<100000:
    commission=(15/100)*target
    print(commission)
elif target>=150000 and target<250000:
    commission=(19/100)*target
    print(commission)
elif target>250000:
    commission=(22/100)*target
    print(commission)
grosspay=(basicpay+commission)
print("The grosspay is:",grosspay)
