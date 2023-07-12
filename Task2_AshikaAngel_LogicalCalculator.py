"""A program to develop a logical calculator with basic operations"""
number1=int(input("Enter the first number:"))#prompting the operands fron the user
number2=int(input("Enter the second nuumber:"))
print("OPERATIONS.. \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Modulo")
number3=int(input("Enter the operation you want to perform:"))#prompting the desired operation from the user
#performing operations using elif statement
if(number3==1):
    add=number1+number2
    print("The result after addition is:",add)
elif(number3==2):
    sub=number1-number2
    print("The result after subtraction is:",sub)
elif(number3==3):
    mul=number1*number2
    print("The result after multiplication is:",mul)
elif(number3==4):
    div=number1/number2
    print("The result after division is:",div)
elif(number3==5):
    mod=number1%number2
    print("The result after modulation is:",mod)
else:
    print("Invalid input...")