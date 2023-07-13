                             #calculating current bill

#prompting current meter and previous meter
cmeter=int(input("enter the current meter:"))
pmeter=int(input("enter the previous meter:"))
unit=cmeter - pmeter
print("the unit :",unit)

if unit<500:
    charges=unit*(3/4)
    print("the amount to be paid is :",charges)
elif unit>=500 and unit<10000:
    charges=unit*(5/4)
    print("the amount to be paid is :",charges)
elif unit>=10000:
    charges=unit*(7/4)
    print("the amount to be paid is :",charges)
    
name=input("Enter you name:")
print(name,".Current charrges for the month :",charges)
