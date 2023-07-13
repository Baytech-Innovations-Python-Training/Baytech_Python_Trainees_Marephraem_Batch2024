name=input("Enter your name: ")
designation=input("Enter your designation: ")
print("Name: ",name)
print("Designation",designation)
if(designation=="Manager"):
    BP=16000    #basic pay
    HR=0.12*BP  #House rent
    DA=0.4*BP   #dearance allowance
    TA=0.09*BP  #Travel allowance
    MA=3000     #medical  alowance
    LIC=1750    #lifr insurance co operation
    PF=0.45*BP  #provident fundn 
    gross_pay=BP+HR+DA+TA+MA
    net_pay=gross_pay-(LIC+PF)
    print("The gross pay is: ",gross_pay)
    print("The net pay is: ",net_pay)
    print("The basic Pay is: ",BP)
elif(designation=="Team Leader"):
    BP=14500
    HR=0.09*BP
    DA=0.37*BP
    TA=0.06*BP
    MA=2250
    LIC=1250
    PF=0.37*BP
    gross_pay=BP+HR+DA+TA+MA
    net_pay=gross_pay-(LIC+PF)
    print("The gross pay is: ",gross_pay)
    print("The net pay is: ",net_pay)
    print("The basic Pay is: ",BP)
elif(designation=="Executive"):
    BP=10000
    HR=0.06*BP
    DA=0.33*BP
    TA=0.045*BP
    MA=1800
    LIC=1000
    PF=0.32*BP
    gross_pay=BP+HR+DA+TA+MA
    net_pay=gross_pay-(LIC+PF)
    print("The gross pay is: ",gross_pay)
    print("The net pay is: ",net_pay)
    print("The basic Pay is: ",BP)
else:
    print("Your Designation is not Difined.........")