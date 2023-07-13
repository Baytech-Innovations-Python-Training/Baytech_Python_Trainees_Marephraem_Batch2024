#create a python program to add ,subtract,multiply ,modulo,divide


a = int(input("Enter a number :"))
b = int(input("Enter another number :"))

print("1: addition,2:subtraction,3:multiplication,4:modulo,5:division")
num=int(input("Choose the operation to be performed:"))

if(num==1):
    add=a+b
    print("The added value is ",add)
elif(num==2):
    sub=a-b
    print("The subtracted value is ",sub)
elif(num==3):
    mul=a*b
    print("The value after multiplication is ",mul)
elif(num==4):
    mod=a%b
    print("The remainder is ",mod)
elif(num==5):
    div=a/b
    print("The divided value is ",div)
else:
    print("Enter a number from 1 to 5 ")






