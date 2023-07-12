#task 2
#calculator
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulo")
choice=int(input("enter your choice:"))
if choice==1:
  result=num1+num2
  print("the result is:",result)
elif choice==2:
  result=num1-num2
  print("the result is:",result)
elif choice==3:
  result=num1*num2
  print("the result is:",result)
elif choice==4:
 if num2!=0:
  result=num1/num2
  print("the result is:",result)
else:
  print("division by zero not allowed")
if choice==5:
 result=num1%num2
 print("the result is:",result)
else:
    print("invalid input")


