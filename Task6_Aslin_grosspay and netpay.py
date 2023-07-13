#salary

name=input("enter the name:")
designation=input("enter your designation:")
if (designation=="manager"):
    basicpay=16000
    houserent=(12/100)*basicpay
    DA=(14/100)*basicpay
    TA=(9/100)*basicpay
    MA=3000
    LIC=1750
    PF=(45/100)*16000
elif (designation=="teamleader"):
    basicpay=14.500
    houserent=(9/100)*basicpay
    DA=(37/100)*basicpay
    TA=(6/100)*basicpay
    MA=2250
    LIC=1250
    PF=(37/100)*14.500
elif (designation=="executive"):
    basicpay=10000
    houserent=(6/100)*basicpay
    DA=(33/100)*basicpay
    TA=(4.5/100)*basicpay
    MA=1800
    LIC=1000
    PF=(32/100)*10000
grosspay=(basicpay+houserent+DA+TA+MA)
totaldeduction=(LIC+PF)
netpay=(grosspay-totaldeduction)
print("enter the name",name)
print("enter the designation",designation)
print("grosspay",grosspay)
print("netpay",netpay)
print("basicpay",basicpay)
