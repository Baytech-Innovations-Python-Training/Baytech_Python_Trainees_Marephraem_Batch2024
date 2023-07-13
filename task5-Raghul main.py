
designation=input("Enter the designation")
name=input("Enter the name")
if designation==manager:
    bp=16000
    houserent=0.12*bp
    da=0.4*bp
    travel=0.9*bp
    ma=3000
    lic=1750
    pf=0.45*bp
    grosspay=bp+houserent+da+travel+ma
    netpay=grosspay-(lic+pf)
    print("The manager",name,designation,grosspay,netpay,bp)
elif designation==teamleader:
    bp=14500
    houserent=0.09*bp
    da=0.37*bp
    travel=0.06*bp
    ma=2250
    lic=1250
    pf=0.37*bp
    grosspay=bp+houserent+da+travel+ma
    netpay=grosspay-(lic+pf)
    print("if teamleader",name,designation,grosspay,netpay,bp)
elif designation==Executive:
    bp=10000
    houserent=0.06*bp
    da=0.33*bp
    travel=0.045*bp
    ma=1800
    lic=1000
    pf=0.32*bp
    grosspay=bp+houserent+da+travel+ma
    netpay=grosspay-(lic+pf)
    print("if execuitive",name,designation,grosspay,netpay,bp)







