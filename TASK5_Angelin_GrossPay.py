                              #calculating gross pay based on commision
#prompting the name
name=input("enter your name:")

#basic pay is decalred
basic_pay=15000

#prompting target_achieved
target_achieved=float(input("enter your target_achieved:"))

#check the target_achieved and calculating commision
if target_achieved<100000:
     commision= target_achieved *(15/100)
     print("commision:",commision)
elif target_achieved>1.50000 and target_achieved<2.50000:
     commision= target_achieved *(19/100)
     print("commision:",commision)
elif target_achieved>2.50000:
    commision= target_achieved *(22/100)
    print("commision:",commision)
    
#calculating the gross pay
gross_pay=basic_pay+commision
print(name,"!your gross pay is given by ",gross_pay)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
