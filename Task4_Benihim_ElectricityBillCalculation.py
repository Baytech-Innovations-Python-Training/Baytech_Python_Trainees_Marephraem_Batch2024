# Inmplement a Program to calculate the Electricity Bill

current_reading=int(input("Enter the Current Reading : "))
previous_reading=int(input("Enter the Previous Reading : "))
current_consumption=current_reading-previous_reading
units=current_consumption
name=str(input("Enter your Name : "))
if(units<500):
    print(name," current charge is : ",units*(3/4))
elif(units>=500 and units<1000):
    print(name," current charge is : ",units*(5/4))
else:
    print(name," current charge is :",units*(7/4))