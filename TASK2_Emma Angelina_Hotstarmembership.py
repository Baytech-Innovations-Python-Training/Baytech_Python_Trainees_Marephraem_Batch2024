#assigning the basic amount to a variable
Membership_payment=499
DAYS=int(input("Enter the no.of days after the due date:"))#getting the input from user
if DAYS==0:#checks if the Days =0
    print("Great!! no fine\nYour total payment is 499")
elif DAYS<=5 and DAYS!=0:#checks the days = 1-5
    print("oops!you are fined\n your total payment is ",Membership_payment+5)
elif DAYS>5 and DAYS<=10:#checks the days = 6-10
    print("oops!you are fined\n your total payment is ",Membership_payment+10)
elif DAYS>10 and DAYS<=15:#checks the days = 11-15
    print("oops!you are fined\n your total payment is ",Membership_payment+15)
else:
    print("SORRY!!! your membership has been cancelled")
