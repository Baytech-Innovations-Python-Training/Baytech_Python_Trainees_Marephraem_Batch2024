#simple calculator
print("!!THE LIST OF OPERATIONS!!")
print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.MODULO")
option=int(input("Choose a Operation to be done:"))
NUM_1=int(input("Enter the first number:"))
NUM_2=int(input("Enter the second number:"))
if option==1:
    print("YOU HAVE CHOSE ADDITION OPERATION!")
    print("RESULT=",NUM_1+NUM_2)
elif option==2:
    print("YOU HAVE CHOSE SUBTRACTION OPERATION!")
    print("RESULT=",NUM_1-NUM_2)
elif option==3:
    print("YOU HAVE CHOSE MULTIPLICATION OPERATION!")
    print("RESULT=",NUM_1*NUM_2)
elif option==4:
    print("YOU HAVE CHOSE DIVISION OPERATION!")
    print("RESULT=",NUM_1/NUM_2)
elif option==5:
    print("YOU HAVE CHOSE MODULO OPERATION!")
    print("RESULT=",NUM_1%NUM_2)
else:
    print("!! INVALID OPTION!!")

