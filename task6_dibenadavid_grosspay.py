name=input("enter the name=")
designation=input("enter the designation=")
if  designation=="manager":
    basicpayment=16000
    homerent=0.16*basicpayment
    dearallovence=0.40*basicpayment
    travelallovence=0.19*basicpayment
    medicalallovance=3000
    lic=1750
    pf=0.45*basicpayment
    td=lic+pf
    grosspay=basicpayment+homerent+ dearallovence+travelallovence+medicalallovance
    netpay=grosspay-td
    print("grosspay=",grosspay)
    print("basicpayment=",basicpayment)
    print("netpay=",netpay)
   
elif designation=="teamleader":
    basicpayment=14500
    homerent=0.9*basicpayment
    dearallovence=0.37*basicpayment
    travelallovence=0.6*basicpayment
    medicalallovance=2250
    lic=1250   
    pf=0.37*basicpayment
    td=lic+pf
    grosspay=basicpayment+homerent+ dearallovence+travelallovence+medicalallovance
    netpay=grosspay-td
    print("grosspay=",grosspay)
    print("basicpayment=",basicpayment)
    print("netpay=",netpay)
   
elif designation=="executive":
    basicpayment=10000   
    homerent=0.6*basicpayment  
    dearallovence=0.33*basicpayment   
    travelallovence=4.5*basicpayment   
    medicalallovance=1800   
    lic=1000    
    pf=0.32*basicpayment
    td=lic+pf
    grosspay=basicpayment+homerent+ dearallovence+travelallovence+medicalallovance
    netpay=grosspay-td
    print("grosspay=",grosspay)
    print("basicpayment=",basicpayment)
    print("netpay=",netpay)
   
else:
    print("invalid designation")


    











    

