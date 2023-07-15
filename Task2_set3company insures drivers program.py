#Company insures drivers program in python
Age=int(input("Enter the Age :"))
Gender=input("Enter the Enter the Gender M/F :")
Martial_Status=input("Enter the Marital Status U/M :")
#using if statement
if Martial_Status=="M":
    print("Driver should be Insured")
elif Martial_Status=="U" and Age>30 and Gender=="M":
    print("Driver should be Insured")
elif Martial_Status=="U" and Age>25 and Gender=="F":
    print("Driver should be Insured")
else:
    print("Driver should not be Insured")
