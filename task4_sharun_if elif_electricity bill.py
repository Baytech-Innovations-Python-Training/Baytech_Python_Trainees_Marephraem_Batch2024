# Electricity bill calculation

name=input("Enter your name:")
current=int(input("Enter the current reading:"))
previous=int(input("Enter the previous reading:"))

unit=current-previous

if (unit<500):
    amount=unit*3/4
elif(unit>=500 and unit<1000):
    amount=unit*5/4
elif(unit>=1000):
    amount=unit*7/4
else:
    print("You have entered the wrong readings")

print("Name:",name,"\nThe amount to be paid is",amount)