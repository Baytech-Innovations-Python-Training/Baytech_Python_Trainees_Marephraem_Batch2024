#Amount for current bill
Name=input("Enter your name: ")
current_reading=int(input("Enter Current Reading: "))
Previous_reading=int(input("Enter previous Reading: "))
current_consumption=current_reading-Previous_reading
if(current_consumption<500):
    a=current_consumption*3/4
    print("the amount is: ",a)
elif(current_consumption>=500 and current_consumption<=1000):
    b=current_consumption*5/4
    print("the amount is: ",b)
elif(current_consumption>=1000):
    c=current_consumption*7/4
    print("the amount is: ",c)
else:
    print("No amount to pay......")
