"""Calculating the salary oof the employee according to there designation"""
name=input("Enter your name:")
designation=input("Enter your designation:")
if(designation=="Manager"):
    bp=16000
    hr=bp*0.12
    da=bp*0.40
    ta=bp*0.09
    ma=3000
    lic=1750
    pf=bp*0.45
    gross_pay=bp+hr+da+ta+ma
    deduction=lic+pf
    print("NAME:",name)
    print("DESIGNATION:",designation)
    print("The BASIC PAY is:",bp)
    print("The GROSS PAY is:",gross_pay)
    print("The NET PAY is:",gross_pay-deduction)
elif(designation=="Team Leader"):
    bp=14500
    hr=bp*0.09
    da=bp*0.37
    ta=bp*0.06
    ma=2250
    lic=1250
    pf=bp*0.37
    gross_pay=bp+hr+da+ta+ma
    deduction=lic+pf
    print("NAME:",name)
    print("DESIGNATION:",designation)
    print("The BASIC PAY is:",bp)
    print("The GROSS PAY is:",gross_pay)
    print("The NET PAY is:",gross_pay-deduction)
elif(designation=="Executive"):
    bp=10000
    hr=bp*0.06
    da=bp*0.33
    ta=bp*0.045
    ma=1800
    lic=1000
    pf=bp*0.32
    gross_pay=bp+hr+da+ta+ma
    deduction=lic+pf
    print("NAME:",name)
    print("DESIGNATION:",designation)
    print("The BASIC PAY is:",bp)
    print("The GROSS PAY is:",gross_pay)
    print("The NET PAY is:",gross_pay-deduction)
else:
    print("Your Designation is not defined..")    

    
    
    
    