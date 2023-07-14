#salary calculation

name=input("Enter your name :")
designation=input("Enter your designation:")
designation=designation.upper()

if (designation=="MANAGER"):
    basic_pay=16000
    house_rent=basic_pay*12/100
    DA=basic_pay*40/100
    travel=basic_pay*9/100
    MA=3000
    LIC=1750
    PF=basic_pay*45/100
elif (designation=="TEAM LEADER"):
    basic_pay=14500
    house_rent=basic_pay*9/100
    DA=basic_pay*37/100
    travel=basic_pay*6/100
    MA=2250
    LIC=1250
    PF=basic_pay*37/100
elif (designation=="EXECUTIVE"):
    basic_pay=10000
    house_rent=basic_pay*6/100
    DA=basic_pay*33/100
    travel=basic_pay*4.5/100
    MA=1800
    LIC=1000
    PF=basic_pay*32/100
else:
    basic_pay=0
    house_rent=0
    DA=0
    travel=0
    MA=0
    LIC=0
    PF=0

gross_pay=basic_pay+house_rent+DA+travel+MA
net_pay=gross_pay-(LIC+PF)

if(gross_pay==0 and net_pay==0):
    print("**************************************************")
    print("ENTER A VALID DESIGNATION!!!!!")
    print("**************************************************")
else:
    print("NAME:",name,"\nDesignation:",designation,"\nGrosspay:",gross_pay,".RS","\nNetpay:",net_pay,".RS","\nBasicpay:",basic_pay ,".RS",)