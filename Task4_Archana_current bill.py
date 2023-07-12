"""
 Current Bill Calculation
Get the Current Reading and Previous Reading of current meter from user.
The difference between the two gives you the total number of Units of Current Consumption.
  If the Unit is less than 500 slab, the amount to be paid is 3/4th of the unit.
If the Unit is greater than or equal to 500 and less than 1000, the amount to be paid is   5/4th of the Unit incurred.
If the unit is greater than or equal to 1000, the amount to be paid is 7/4th of the unit  incurred.
Finally print the name of the user and his current charges for the month depending on his slab."""




name=input("Enter the name:")
cr=int(input("Enter the current reading:"))
pr=int(input("Enter the previous reading:"))
unit=cr-pr
print("totalunits:",unit)
if(unit<500):
    print("The current charge of the month:",unit*(3/4))
if(500<=unit<1000):
    print("The current charge of the month:",unit*(5/4))
if(unit>=1000):
    print("The current charge of the month:",unit*(7/4))

    


