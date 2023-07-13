                   # to check prime hotstar membership fine
                   
#prompting date
membership=input("enter the membership expire date:")
#prompting remainig_days
remainig_days=int(input("enter number of days remaining for your prime hotstar membership: "))

#declare membership amount
amount=500
print("the membership amount is given by:",amount)

#to check fine amount
if remainig_days==0:
    print("goood,no fine")
elif remainig_days>0 and remainig_days<=5:
    print("fine amount:",amount+5)
elif remainig_days>5 and remainig_days<=10:
    print("fine amount:",amount+10)
elif remainig_days>10 and remainig_days<=30:
    print("fine amount:",amount+10)
else :
    print(" your membership has been cancel!!!")


                          
