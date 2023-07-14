#calculator
#this note gives a idea about the operation shortcut
note= """Enter A for Addition Operation
Enter S for Subtraction Operation
Enter D for Divition Operation
Enter M for Multiplication Operation
Enter mo for Modulo Operation"""
print (note)
#user selects a operation using shortcut
o=str(input("Enter the Operation :"))
#if we enter A addition is done 
if o=="A":
    a=int(input("Enter the value :"))
    b=int(input("Enter the value :"))
    print (a+b)
#if we enter S subtraction is done     
elif o=="S":
    a=int(input("Enter the value :"))
    b=int(input("Enter the value :")) 
    print (a-b)
#if we enter D divition is done 
elif o=="D":
    a=int(input("Enter the value :"))
    b=int(input("Enter the value :"))
    print (a/b)    
#if we enter M multiplication is done 
elif o=="M":
    a=int(input("Enter the value :"))
    b=int(input("Enter the value :"))
    print (a*b)
#if we enter mo modulo is done
elif o=="mo":
    a=int(input("Enter the value :"))
    b=int(input("Enter the value :"))
    print (a%b)
"""if we enter any other input except
    the defined ones it will show as syntax error"""
else:
    print ("Syntax Error")

