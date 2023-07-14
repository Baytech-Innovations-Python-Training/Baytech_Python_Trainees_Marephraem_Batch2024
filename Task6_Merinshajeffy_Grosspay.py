#FIND THE ROLE
a=input("The name of the employee")
name=input("enter the name:")
if name=="Manager":
    basicpay=16000
    houseallowance=12/100*basicpay
    DA=40/100*basicpay
    travel=9/100*basicpay
    MA=3000
    LIC=1750
    PF=45/100*basicpay
elif name=="Team Leader":
    basicpay=14500
    houseallowance=9/100*basicpay
    DA=3/100*basicpay
    travel=6/100*basicpay
    MA=2250
    LIC=1250
    PF=37/100*basicpay
elif name=="Exective":
    basicpay=10000
    houseallowance=6/100*basicpay
    DA=33/100*basicpay
    travel=4.5/100*basicpay
    MA=1800
    LIC=1000
    PF=32/100*basicpay
Grosspay=(basicpay+houseallowance+travel++DA+MA)
print("The gross pay:",Grosspay)
netpay=Grosspay-(LIC+PF)
print("The basicpay is:",basicpay)
print("The net pay is:",netpay)"""
