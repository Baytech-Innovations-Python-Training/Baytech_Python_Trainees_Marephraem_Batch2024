# calculating the salary by his/her designation

name=input("Enter your name : ") #promting name from user
print("DESIGNATIONS","\n","* Manager","\n","* Team Leader","\n","* Executive")
D=input("Your Designation : ") #promting the user to choose designation

if D=="Manager": #it compares the variable D is having the value "Manager",if it is correct it executes the following if statement
    Basic_Pay=16000
    House_rent=Basic_Pay*12/100
    Dearest_Allowance=Basic_Pay*40/100
    Travel_Allowance=Basic_Pay*9/100
    M_A=3000
    P_F=Basic_Pay*45/100
    LIC=1750
elif D=="Team Leader":
    Basic_Pay=14500
    House_rent=Basic_Pay*9/100
    Dearest_Allowance=Basic_Pay*37/100
    Travel_Allowance=Basic_Pay*6/100
    M_A=2250
    P_F=Basic_Pay*37/100
    LIC=1250
elif D=="Executive":
    Basic_Pay=10000
    House_rent=Basic_Pay*6/100
    Dearest_Allowance=Basic_Pay*33/100
    Travel_Allowance=Basic_Pay*4.5/100
    M_A=1800
    P_F=Basic_Pay*32/100
    LIC=1000
else:
    Basic_Pay = 0
    House_rent = 0
    Dearest_Allowance = 0
    Travel_Allowance = 0
    M_A = 0
    P_F = 0
    LIC = 0

gross_pay=Basic_Pay+House_rent+Dearest_Allowance+Travel_Allowance+M_A
net_pay=gross_pay - (P_F+LIC)
if gross_pay==0 and net_pay==0: # if these variables are "0" it won't execute else statement
    print("\nPlease Enter Designation Correctly \n(uppercase, lowercase and spelling also checked)")
else:
    #output
    print("\n\n""Name of the Employee is ",name,"\n""You have selected your designation as ",D)
    print("Your Gross Pay will be  ",gross_pay,"\n""your Net Pay will be ",net_pay,"\n""Your Basic Salary will be ",Basic_Pay)



