#calculate salary program in python
Gender=input("Enter the Gender f/m :")
Years_of_service=int(input("Enter the Years of Service :"))
Qualification=int(input("Enter the Qualification (Graduate(0) , Post-Graduate(1)) :"))
#using if condition to check male salary
if Gender=="m":
    if Years_of_service>=10 and Qualification==1:
        print("Salary :15000")
    elif Years_of_service>=10 and Qualification==0:
        print("Salary :10000")
    elif Years_of_service<10 and Qualification==1:
        print("Salary :10000")
    else:
        print("Salary :7000")
#using if condition to check female salary
if Gender=="f":
    if Years_of_service>=10 and Qualification==1:
        print("Salary :12000")
    elif Years_of_service>=10 and Qualification==0:
        print("Salary :9000")
    elif Years_of_service<10 and Qualification==1:
        print("Salary :10000")
    else:
        print("Salary :6000")
