#calculator
calculate
num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if num3==1:
    print("1 for addition")
    print(num1+num2)
elif num3==2:
    print("2 for sub")
    print(num1-num2)
elif num3==3:
    print("3 for multiplication")
    print(num1*num2)
elif num3==4:
    print("4 for divide")
    print(num1/num2)
elif num3==5:
    print("5 for modulo")
    print(num1%num2)
else:
    print("invalid number")
