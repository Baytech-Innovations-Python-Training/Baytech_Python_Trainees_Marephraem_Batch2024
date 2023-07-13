#Salary Calculation based on the target achieved
"""Get the name and target achieved from the user by prompting and the basic pay of the user is given"""
Name=input("Enter the name:")
Target_achieved=int(input("Enter the target value:"))
Basic_pay=15000
"""Using the if condition check the target achieved and compute the commission"""
if(Target_achieved<100000):
    Commission=Target_achieved*15/100
elif(Target_achieved>=100000 and Target_achieved<=250000):
    Commission=Target_achieved*19/100
elif(Target_achieved>250000):
    Commission=Target_achieved*22/100
else:
    print("No Commission")
"""Gross pay is the sum of basic pay and commission"""
Gross_pay=Basic_pay+Commission
print("Employee Name:",Name)
print("Gross_pay:",Gross_pay)
    
