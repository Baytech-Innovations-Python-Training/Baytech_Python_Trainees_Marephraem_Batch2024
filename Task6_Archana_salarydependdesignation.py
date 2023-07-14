#based on the designation it will calculate salary
Name=input("Enter the name:")
designation=input("Enter the position:")

if(designation=="manager"):
    bp=16000
    hr=(12/100)*bp
    da=(40/100)*bp
    ta=(9/100)*bp
    ma=3000
    lic=1750
    pf=(45/100)*bp
    td=lic+pf


elif(designation=="teamleader"):
    bp=14500
    hr=(9/100)*bp
    da=(37/100)*bp
    ta=(6/100)*bp
    ma=2250
    lic=1250
    pf=(37/100)*bp
    td=lic+pf

elif(designation=="executive"):
    bp=10000
    hr=(6/100)*bp
    da=(33/100)*bp
    ta=(4.5/100)*bp
    ma=1800
    lic=1000
    pf=(32/100)*bp
    td=lic+pf
    
grosspay=bp+hr+da+ta+ma
np=grosspay-td
print("name:",Name)
print("designation:",designation)
print("grosspay:",grosspay)
print("basicpay:",bp)
print("netpay:",np)
