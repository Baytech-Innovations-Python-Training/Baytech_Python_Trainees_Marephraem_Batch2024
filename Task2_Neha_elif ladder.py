#calculator
#elif ladder
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
#operations
print("1.Add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.modulo")
choice=int(input("Enter your choice:"))
if choice==1:
    result=a+b
    print("The result is:",result)
elif choice==2:
    result=a-b
    print("The result is:",result)
elif choice==3:
    result=a*b
    print("The result is:",result)
elif choice==4:
    if b!=0:
     result=a/b
     print("The result is:",result)       
    else:
     print("Error:Division by zero is undefined")
elif choice==5:
    result=a%b
    print("The result is:",result)
else:
    print("Invalid")
