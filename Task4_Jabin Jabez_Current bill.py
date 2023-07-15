current_reading=int(input("Enter the current reading:"))
previous_reading=int(input("Enter the previous reading:"))
name=input("Name of the user:")
total_unit=previous_reading-current_reading
if(total_unit<500):
    print("The amount to be paid is:",total_unit*3/4)
elif(total_unit>=500 and total_unit<1000):
    print("The amount to be paid is:",total_unit*5/4)
else:
    print("The amount to be paid is:",total_unit*7/4)