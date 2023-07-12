#Current Bill Calculation
name=input("Enter the name:")
currentreading=int(input("Enter the current reading:"))
previousreading=int(input("Enter the previous reading:"))
unit=currentreading-previousreading
print("unit:",unit)
if unit<500:
 print("The amount:",unit*3/4)
elif unit>=500 and unit<1000:
 print("The amount:",unit*5/4)
elif unit>=1000:
 print("The amount:",unit*7/4)
else:
  print("unit is not acceptable")  
