#calculating amount for eb bill
name=input("enter the customer name:")
current=int(input("enter the current:"))
previous=int(input("enter the previous:"))
print("Eb bill for ",name)
unit=current-previous
if unit<500:
    print("the amount to pay=",unit*3/4)
elif unit>=500 and unit<1000:
    print("the amount to pay=",unit*5/4)
elif unit>=1000:
    print("the amount to pay=",unit*7/4)
else:
    print("unit is invalid")
