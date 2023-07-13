a=int(input("Enter the current reading"))
b=int(input("Enter the previous reading"))
name=input("Enter the name")
unit=a-b
if(unit<500):
    print("The amount paid",name,unit*0.75)
elif(unit>=500 and unit<=1000):
    print("The amount paid",name,unit*1.25)
elif(unit>1000):
    print("The amount paid",name,unit*1.74)
else:
    print("unit not accept")
