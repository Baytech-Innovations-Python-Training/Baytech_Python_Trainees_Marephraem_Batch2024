NAME=input("Enter Your Name:")
print("!!select your designation!!")
print("1.MANAGER\n2.TEAM LEADER\n3.EXECUTIVE")
designation=int(input(("Choose an designation:")))
print("SALARY DETAILS!!!")
if designation==1:
    print("NAME:",NAME)
    print("DESIGNATION: MANAGER")
    print("BASIC PAY=16000")
    BASIC_PAY=16000
    HR=16000*12/100
    DA=16000*40/100
    TA=16000*9/100
    PF=16000*45/100
    MA=3000
    LIC=1750
    Grosspay=BASIC_PAY+HR+TA+DA+MA
    print("Grosspay=",Grosspay)
    print("Netpay=",Grosspay-(LIC+PF))
    
elif designation==2:
    print("NAME:",NAME)
    print("DESIGNATION: TEAM LEADER")
    print("BASIC PAY=14500")
    BASIC_PAY=14500
    HR=14500*9/100
    DA=14500*37/100
    TA=14500*6/100
    PF=14500*37/100
    MA=2250
    LIC=1250
    Grosspay=BASIC_PAY+HR+TA+DA+MA
    print("Grosspay=",Grosspay)
    print("Netpay=",Grosspay-(LIC+PF))
elif designation==3:
    print("NAME:",NAME)
    print("DESIGNATION:EXECUTIVE")
    print("BASIC PAY=10000")
    BASIC_PAY=10000
    HR=10000*6/100
    DA=10000*33/100
    TA=10000*4.5/100
    PF=10000*32/100
    MA=1800
    LIC=1000
    Grosspay=BASIC_PAY+HR+TA+DA+MA
    print("Grosspay=",Grosspay)
    print("Netpay=",Grosspay-(LIC+PF))
else:
    print("your option is ivalid")
 
