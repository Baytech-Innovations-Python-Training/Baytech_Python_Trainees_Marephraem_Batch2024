"""Calculating the amount to be paid for EB bill"""
name=input("Enter your name:")#prompting the basic details
cur_reading=int(input("Enther the current reading:"))
pre_reading=int(input("Enther the previous reading:"))
print("EBill for",name)
cur_consumption=cur_reading-pre_reading
if(cur_consumption<500):
    print("The amount to pay =",cur_consumption*3/4)
elif(cur_consumption>=500 and cur_consumption<1000):
    print("The amount to pay=",cur_consumption*5/4)
elif(cur_consumption>=1000):
    print("The amount to pay=",cur_consumption*7/4)  
else:
    print("Unit is not acceptable..")
      
    