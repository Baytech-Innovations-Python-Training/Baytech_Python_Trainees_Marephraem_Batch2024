#program for salery for manager,teamleader,executive
designation=input("Enter the designation:")
name=input("Enter the name:")
if designation=="manager":
    BP=16000
    HR=0.12*BP
    DA=0.4*BP
    TA=0.9*BP
    MA=3000
    LIC=1750
    PF=0.45*BP
    grosspay=BP+HR+DA+TA+MA
    netpay=grosspay-(LIC+PF)
    print("team manager",name,designation,grosspay,netpay,BP)
elif designation=="teamleader":
    BP=14500
    HR=0.09*BP
    DA=0.37*BP
    TA=0.06*BP
    MA=2250
    LIC=1250
    PF=0.37*BP
    grosspay=BP+HR+DA+TA+MA
    netpay=grosspay-(LIC+PF)
    print("teamleader",name,designation,grosspay,netpay,BP)
elif designation=="executive":
    BP=10000
    HR=0.06*BP
    DA=0.33*BP
    TA=0.045*BP
    MA=1800
    LIC=1000
    PF=0.32*BP
    grosspay=BP+HR+DA+TA+MA
    netpay=grosspay-(LIC+PF)
    print("team execution",name,designation,grosspay,netpay,BP)