#Program to perform current bill calculation
"""Get the name of the user,current reading and previous reading of the current meter from the user by prompting"""
Name=input("Enter the name:")
Current_reading=int(input("Enter the Current reading:"))
Previous_reading=int(input("Enter the Previous reading:"))
"""The difference between the current reading and previous reading gives the total number of units of current consumed"""
Unit=Current_reading-Previous_reading
print("Current Bill to be paid by",Name)
"""Using the if condition check the amount that has to be paid by the user"""
if(Unit<500):
    amount=3/4*Unit
    print("The amount is",amount)
elif(Unit>=500 and Unit<1000):
    amount=5/4*Unit
    print("The amount is ",amount)
else:
    amount=7/4*Unit
    print("The amount is",amount)
