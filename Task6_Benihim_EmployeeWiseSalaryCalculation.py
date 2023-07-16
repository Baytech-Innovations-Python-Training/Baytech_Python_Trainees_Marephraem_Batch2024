#Implement a Program to find the employeewise salary calculation

name=str(input("Enter your Name : "))
designation=str(input("Enter your Designation : "))
if designation=="Manager":
    basic_pay=16000
    ha=basic_pay*(12/100)
    da=basic_pay*(40/100)
    ta=basic_pay*(9/100)
    ma=3000
    LIC=1750
    pf=basic_pay*(45/100)
    gross_pay=basic_pay+ha+da+ta+ma
    net_pay=basic_pay-(LIC+pf)
    print(f"{name} is a {designation} who got"
          f" \n Gross Pay : {gross_pay} "
          f"\n Net Pay : {net_pay} "
          f"\n Basic Pay = {basic_pay}")
elif designation=="Team Leader":
    basic_pay = 14500
    ha = basic_pay * (9 / 100)
    da = basic_pay * (37 / 100)
    ta = basic_pay * (6 / 100)
    ma = 2250
    LIC = 1250
    pf = basic_pay * (37 / 100)
    gross_pay = basic_pay + ha + da + ta + ma
    net_pay = basic_pay - (LIC + pf)
    print(f"{name} is a {designation} who got"
          f" \n Gross Pay : {gross_pay} "
          f"\n Net Pay : {net_pay} "
          f"\n Basic Pay = {basic_pay}")
elif designation=="Executive":
    basic_pay = 10000
    ha = basic_pay * (6 / 100)
    da = basic_pay * (33 / 100)
    ta = basic_pay * (4.5 / 100)
    ma = 1800
    LIC = 1000
    pf = basic_pay * (37 / 100)
    gross_pay = basic_pay + ha + da + ta + ma
    net_pay = gross_pay -( LIC + pf )
    print(f"{name} is a {designation} who got"
          f" \n Gross Pay : {gross_pay} "
          f"\n Net Pay : {net_pay} "
          f"\n Basic Pay = {basic_pay}")
else:
    print("......Invalid Designation......")