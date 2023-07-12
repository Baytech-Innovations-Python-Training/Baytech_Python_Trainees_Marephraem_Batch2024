#Elif ladder
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
n=int(input("Enter the num:"))
if n==1:
    print("To add two number",a+b)
elif n==2:
    print("To sub two nos",a-b)
elif n==3:
    print("To multiply two nos",a*b)
elif n==4:
    print("To divide two",a/b)
elif n==5:
    print("To modulo",a%b)
else:
    print("invalid")