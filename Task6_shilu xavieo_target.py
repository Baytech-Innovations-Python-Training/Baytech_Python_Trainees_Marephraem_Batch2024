#office designation
designation=input("enter your designation:")
name=input("enter your name")
if designation=="manager":
    basicpay=1600
    houserentallowance=12/100*basicpay
    DA=40/100*basicpay
    travelallowance=9/100*basicpay
    MA=3000
    LIC=1750
    PF=45/100*basicpay
elif designation=="teamleader":
    basicpay=14500
    houserentallowance=9/100
    DA=37/100
    travelallowance=6/100
    MA=2250
    LIC=1000
    PF=37/100
elif designation=="Executive":
    basicpay=10000
    houserentallowance=6/100*basicpay
    DA=33/100*basicpay
    travelallowance=4.5/100*basicpay
    MA=1800
    LIC=1000
    PF=32/100*basicpay
grosspay=(basicpay+houserentallowance+DA+travelallowance+MA)
print("grosspay:",grosspay)
netpay=grosspay-(LIC+PF)
print("netpay:",netpay)
print("basicpay:",basicpay)
