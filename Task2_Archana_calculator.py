"""

Calculator 

1.Add 
2.Sub
3.Mul
4.Div
5.Modulo 
 
Get 2 numbers. Ask for user's choice.
Depending on choice do the respective operation   else print as invalid input

#Elif ladder"""







#Calculator program
a=int(input("Enter the number"))
b=int(input("Enter the number"))
num=int(input("Enter the number"))

if(num==1):
    print(a+b)
elif(num==2):
    print(a-b)
elif(num==3):
    print(a*b)
elif(num==4):
    print(a/b)
elif(num==5):
    print(a%b)
else:
    print("invalid input")

