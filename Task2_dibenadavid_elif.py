#task2
"""Task 2

Calculator 

1.Add 
2.Sub
3.Mul
4.Div
5.Modulo

Get 2 numbers. Ask for user's choice. Depending on choice do the respective operation   else print as invalid input

#Elif ladder"""                

a=int(input("enter the first number="))
b=int(input("enter the second number="))
c=int(input("enter the arthmetic operation you want="))
if c==1:
    print("add=",a+b)
elif c==2:
    print("sub=",a-b)
elif c==3:
    print("mult=",a*b)
elif c==4:
    print("div=",a/b)
elif c==5:
    print("modulo=",a%b)      
else:
    print("invalied")










