a=int(input("Enter the value 1:"))
b=int(input("Enter the value 2:"))
print("1.Add"'\n'"2.Sub"'\n'"3.Mul"'\n'"4.Div"'\n'"5.Modulo")
n=int(input("Enter the number:"))
if(n==1):
    c=a+b
    print(c)
elif(n==2):
    c=a-b
    print(c)
elif(n==3):
    c=a*b
    print(c)
elif(n==4):
    c=a/b
    print(c)
elif(n==5):
    c=a%b
    print(c)
else:
    print("invalid input")