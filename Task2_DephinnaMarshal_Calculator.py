#simple Calculator
Num1=int(input("Enter first Number:"))
Num2=int(input("Enter Second Number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulo")
Operation=int(input("Select the operation you want to perform:"))
if Operation==1:
    print("The Result is:",Num1+Num2)
elif Operation==2:
    print("The Result is:",Num1-Num2)
elif Operation==3:
    print("The Result is:",Num1*Num2)
elif Operation==4:
    print("The Result is:",Num1/Num2)
elif Operation==5:
    print("The Result is:",Num1%Num2)
else:
    print("Your Option is Invalid!!")
        
