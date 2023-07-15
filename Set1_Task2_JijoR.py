#Youngest age of three program
age1=int(input("Enter the age of Ram:"))
age2=int(input("Enter the age of Shyam:"))
age3=int(input("Enter the age of Ajay:"))
if age1<age2 and age1<age3:
    print("The youngest age is Ram.")
elif age2<age1 and age2<age3:
    print("The youngest is Shyam.")
else:
    print("The youngest is Ajay.")
