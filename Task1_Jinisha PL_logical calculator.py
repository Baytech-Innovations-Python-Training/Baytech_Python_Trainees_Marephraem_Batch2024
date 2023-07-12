num1=int(input("enter a number: "))
num2=int(input("enter another number: "))
print("operations... \n 1.additon \n 2.subraction \n 3.multiplication \n 4.division \n 5.modulo")
num3=int(input("enter a operation: "))
if(num3==1):
    a=num1+num2
    print("The sum is: ",a)
elif(num3==2):
    b=num1-num2
    print("The difference is: ",b)
elif(num3==3):
    c=num1*num2
    print("The product is: ",c)
elif(num3==4):
    d=num1/num2
    print("The quotient is: ",d)
elif(num3==5):
    e=num1%num2
    print("The reminder is: ",e)
else:
    print("nothing")  