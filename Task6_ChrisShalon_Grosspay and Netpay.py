#To find the Gross pay and Net pay of an employee based upon the designation
"""Get the name and designation from the user by prompting"""
Name=input("Enter the name:")
designation=input("Enter the designation:")
"""Check the designation and its allowances using if condition"""
if(designation=="Manager"):
    BP=16000
    HR=12/100*BP
    DA=40/100*BP
    TA=9/100*BP
    MA=3000
    LIC=1750 
    PF=45/100*BP
elif(designation=="Team Leader"):
    BP=14500
    HR=9/100*BP
    DA=37/100*BP
    TA=6/100*BP
    MA=2250
    LIC=1250 
    PF=37/100*BP
elif(designation=="Executive"):
    BP=10000
    HR=6/100*BP
    DA=33/100*BP
    TA=4.5/100*BP
    MA=1800
    LIC=1000 
    PF=32/100*BP    
else:
    print("Invalid")
"""Compute the total deduction,gross pay and net pay"""   
Total_Deductions=(LIC+PF)
GP=BP+HR+DA+TA+MA
NP=GP-Total_Deductions
print("Employee Name:",Name)
print("Designation:",designation)
print("Gross pay:",GP)
print("Net Pay:",NP)
print("Basic Pay:",BP)
