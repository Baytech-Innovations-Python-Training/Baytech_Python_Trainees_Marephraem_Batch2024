"""Program for prompting the expiry of amazon prime subscription and displaying the fine amount"""
sub_amount=399
subForMemEx=499
name=input("Enter your name:")#prompting subscriber name
print("Enter the count of the present day from the epiry of amazon prime subscription...")
days=int(input("number of days:"))#prompting the no.of days of expiry
#conditions for fine in conditioning statements
if(days==0):
    print("No fine for 0 days subcription renewal amount=",sub_amount)
elif(days>0 and days<=5):
    print("The fine amount is 5RS \n subcription renewal amount=",sub_amount+5)
elif(days>5 and days<=10):
    print("The fine amount is 10RS \n subcription renewal amount=",sub_amount+10)
elif(days>10 and days<=30):
    print("The fine amount is 15RS \n subcription renewal amount=",sub_amount+15)
else:
    print("Membership Expired... \n subcription amount=",subForMemEx)