#current bill
currentreading=int(input("Enter the current amount:"))
previousreading=int(input("Enter the previous amount:"))
name=input("Enter the name:")
unit=currentreading-previousreading
if(unit<500):
    print("The amount paid",name,unit*0.75)
elif(unit>=500 and unit<=1000):
    print("The amount paid",name,unit*1.25)
elif(unit>=1000):
    print("The amount paid",name,unit*1.74)
else:
    print("unit not accept")