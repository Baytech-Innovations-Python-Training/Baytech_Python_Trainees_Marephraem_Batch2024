# Implement a program to find the Gross pay of a Employee

baisc_pay=15000
name=str(input("Enter Employee Name : "))
target_acheived=str(input("Enter the target value acheived : "))

if target_acheived<=100000:
    gross_pay=target_acheived*(15/100)
    print(f"{name}'s Gross Pay is {gross_pay}")
elif target_acheived>100000 and target_acheived<=250000:
    gross_pay=target_acheived*(19/100)
    print(f"{name}'s Gross Pay is {gross_pay}")
elif target_acheived>250000:
    gross_pay=target_acheived*(22/100)
    print(f"{name}'s Gross Pay is {gross_pay}")
else:
    print('INVALID COST')