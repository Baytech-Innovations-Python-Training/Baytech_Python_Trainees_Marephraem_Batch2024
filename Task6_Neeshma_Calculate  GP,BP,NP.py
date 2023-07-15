#Calculating a GP,BP,NP
name=input("Enter the Name:")
designation=(input("Enter the Designation:"))
if(designation=="Manager"):
    BR=16000
    HR=0.12*16000
    DA=0.4*16000
    TA=0.09*16000
    MA=3000
    LIC=1750
    PF=0.45*16000
    grosspay=BR+HR+DA+TA+MA
    deduction=(LIC+PF)
    print("The name is",name)
    print("The designation is",designation)
    print("The grosspay is",BR+HR+DA+TA+MA)
    print("The Netpay is",grosspay-(LIC+PF))
    print("The basic pay is",BR)
elif (designation == "Team Leader"):
        BR = 14500
        HR = 0.09 * 14500
        DA = 0.37* 14500
        TA = 0.06 * 14500
        MA = 2250
        LIC = 1250
        PF = 0.37 * 14500
        grosspay = BR + HR + DA + TA + MA
        deduction = (LIC + PF)
        print("The name is", name)
        print("The designation is", designation)
        print("The grosspay is", BR + HR + DA + TA + MA)
        print("The Netpay is", grosspay - (LIC + PF))
        print("The basic pay is", BR)
elif(designation=="Exceutive"):
    BR=10000
    HR=0.06*10000
    DA=33/100*10000
    TA=4.5/100*10000
    MA=18000
    LIC=1000
    PF=32/100 *16000
    grosspay = BR + HR + DA + TA + MA
    deduction = (LIC + PF)
    print("The name is",name)
    print("The designation is",designation)
    print("The grosspay is",BR+HR+DA+TA+MA)
    print("The Netpay is",grosspay-(LIC+PF))
    print("The basic pay is", BR)
