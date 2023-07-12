#program to find positive or negative number
num1=int(input("enter a number: "))
if(num1>0):
    if(num1%2==0):
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
elif(num1==0):
    print("The number is neutral")
else:
    if(num1%2==0):
        print("The number negative and even")
    else:
        print("The number is negative and odd")