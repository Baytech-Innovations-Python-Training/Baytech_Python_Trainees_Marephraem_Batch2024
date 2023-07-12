#current bill
name=input("enter the name:")
currentreading=int(input("enter the current reading:"))
previousreading=int(input("enter the previous reading:"))
unit=(currentreading-previousreading)
print(unit)
if unit<500:
 print(unit*3/4)
elif(unit>=500 and unit<1000):
 print(unit*5/4)
elif(unit>=1000):
 print(unit*7/4)
