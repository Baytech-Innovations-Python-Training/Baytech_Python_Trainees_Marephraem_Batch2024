# Implement a Program to Choose the option and done the Arithmetic Operations

print("Options: \n1.Addition \n2.Subraction \n3.Multiplication \n4.Division \n5.Modulo")
options=int(input("Enter a Option : "))
a=int(input("Enter a Number : "))
b=int(input("Enter a Number : "))
if options==1 :
    print("The Addition of the give number is ",a+b)
elif options==2 :
    print("The Subraction of the give number is ",a-b)
elif options==3 :
    print("The Multiplication of the give number is ",a*b)
elif options==4 :
    print("The Division of the give number is ",a/b)
elif options==5 :
    print("The Modulo of the given number is ",a%b)
else:
    print("Invalid Option")