#current bill

name=input("enter the name=")
current=int(input("enter the current reading value="))
prives=int(input("enter the prives reading value="))
bill=current-prives
print("bill=",bill)
if bill<500:
    total=bill*3/4
    print("CURREND CHARGE=",total)
elif bill>=500<1000:
    total1=bill*5/4
    print("CURREND CHARGE=",total1)
elif bill>=1000:
    total2=bill*7/4
    print("CURREND CHARGE=",total2)



    
