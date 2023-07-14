                                #calculation of salary based on designation

#prompting the name                  
name=input("enter your name:")

#print designation
print("the designations are given by:")
print("manager")
print("team leader")
print("executive")
designation=input("enter your designation:")

# to check designation and declared values for each
if designation == "manager":
    basic_pay=16000
    house_rent=basic_pay*(12/100)
    dearance_allowance=basic_pay*(40/100)
    travel_allowance=basic_pay*(9/100)
    medical_allowance=30000
    Lic=1750
    provident_fund=basic_pay*(45/100)
elif designation=="team leader":
    basic_pay=14500
    house_rent=basic_pay*(9/100)
    dearance_allowance=basic_pay*(37/100)
    travel_allowance=basic_pay*(6/100)
    medical_allowance=2250
    Lic=1250
    provident_fund=basic_pay*(37/100)
elif designation== "executive":
    basic_pay=10000
    house_rent=basic_pay*(16/100)
    dearance_allowance=basic_pay*(33/100)
    travel_allowance=basic_pay*(4.5/100)
    medical_allowance=1300
    Lic=1000
    provident_fund=basic_pay*(32/100)
else:
    print("opps!give the correct designation")

#calculate gross pay,net pay
gross_pay=basic_pay+house_rent+dearance_allowance+travel_allowance+medical_allowance
total_deduction=Lic+provident_fund
net_pay=gross_pay-total_deduction #total_deduction=Lic+provident_fund


print("***************************")

#print statement
print("your name is:",name)
print("your designation is: ",designation)
print("your GrossPay is given by:",gross_pay  )
print("your NetPay is given by:",net_pay)
print("and your basic pay is given by:",basic_pay)

print("***************************")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
