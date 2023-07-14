"""The Gross pay of the employee based on his target achieved"""
basic_pay=15000
name=input("Enter your name:")
target_achieved=int(input("enter the target you achieved:"))
print("Name:",name)
if(target_achieved<100000 and target_achieved>0):
    commission=target_achieved*0.15
    print("Your Gross pay is:",basic_pay+commission)
elif(target_achieved>=100000 and target_achieved<250000):
    commission=target_achieved*0.19
    print("Your Gross pay is:",basic_pay+commission)
else:
    commission=target_achieved*0.22
    print("Your Gross pay is:",basic_pay+commission)