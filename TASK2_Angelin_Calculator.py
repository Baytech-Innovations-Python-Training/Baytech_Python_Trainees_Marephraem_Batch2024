                                   #calculator - uing elif ladder
    
#prompting two numbers
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("*****************************")
#choices
print(" Choice is mention as below")
print(" enter 1 for addition")
print(" enter 2 for subtraction")
print(" enter 3 for  multiplication")
print(" enter 4 for division")
print(" enter 5  for modulo")
print("*****************************")
choice=int(input("enter your choice:"))
#addition
if choice==1:
    print("you have entered the choice 1")
    print("Addition of given two number is:",num1+num2)
#subtraction
elif choice==2:
    print("you have entered the choice 2")
    print("subtraction of two numbers is :",num1-num2)
#multiplication
elif choice==3:
    print("you have entered the choice 3")
    print("multiplication of two numbers is :",num1*num2)
#division
elif choice==4:
    print("you have entered the choice 4")
    print(" division of two numbers is :",num1/num2)
#modulo
elif choice==5:
    print("you have entered the choice 5")
    print("modulo of two numbers is  :",num1%num2)
#invalid
else:
    print("The number is invalid!")
    print("please,enter the number between 1 to 5")
