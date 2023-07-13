#salary calculation
#based on designation
#getting name and designation from the user
name=input("Enter the Name:")
designation=input("Enter the Designation:")
if(designation=="manager"):
    BP=16000
    HR=(12/100)*BP
    DA=(40/100)*BP
    TA=(9/100)*BP
    MA=3000
    LIC=1750
    PF=(45/100)*BP
elif(designation=="teamleader"):
     BP=14500
     HR=(9/100)*BP
     DA=(37/100)*BP
     TA=(6/100)*BP
     MA=2250
     LIC=1250
     PF=(37/100)*BP
elif(designation=="executive"):
     BP=10000
     HR=(6/100)*BP
     DA=(33/100)*BP
     TA=(4.5/100)*BP
     MA=1800
     LIC=1000
     PF=(32/100)*BP
grosspay=BP+HR+DA+TA+MA
totaldeduction=LIC+PF
netpay=grosspay-totaldeduction
print("Name of the Employee:",name)
print("Designation of Employee:",designation)
print("The grosspay:",grosspay)
print("The netpay:",netpay)
print("The Basic pay:",BP)
