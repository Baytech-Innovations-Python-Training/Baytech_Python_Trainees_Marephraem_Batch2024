#Calculating a Salary
Name=(input("Enter the Name:"))
Basic_pay=int(input("Enter the Basic pay:"))
Target=int(input("Enter the Target:"))

if Target<100000:
    Commission = Target * 0.15
    print("The Commission is:",Target*0.15)
elif Target>=150000 and Target<=250000:
    Commission = Target * 0.19
    print("The Commission is:",Target*0.19)
else:
    Commission = Target * 0.22
    print("The Commission is:",Target*0.22)
print(Name)
print("The Salary is",Basic_pay+Commission)









