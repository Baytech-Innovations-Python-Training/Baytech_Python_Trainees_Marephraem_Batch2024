#Calculator program using elif ladder
"""Get three values from the user by promping ,where variable is used to get the choice of the operation and variables b and c are used to get first and second values of the operation"""
a=int(input("Enter the value to choose the arithematic operation :"))
b=int(input("Enter the first value :"))
c=int(input("Enter the second value :"))
"""Elif ladder statement is used ,to show the conditions and there operations"""
if(a==1):
    add=b+c
    print("Addition:",add)
elif(a==2):
    sub=b-c
    print("Subtraction:",sub)
elif(a==3):
    mul=b*c
    print("Multiplication:",mul)
elif(a==4):
    div=b/c
    print("Division:",div)
elif(a==5):
    mod=b%c
    print("Modulo:",mod)
else:
    print("Invalid")
