#Prime Hotstar MemberShip Fine Amount Calculation
Subscription_amount=399 
Days=int(input("Enter the number of days till today since your subscription has been expired:"))#Getting input from the user
if(Days==0):
    print("Good!,You have no fine,Your payment amount is",Subscription_amount)
elif(1<=Days<=5):
    print("Your fine amount is ₹",5+Subscription_amount)
elif(6<=Days<=10):
    print("Your fine amount is ₹",10+Subscription_amount)
elif(11<=Days<=30):
    print("Your fine amount is ₹",15+Subscription_amount)
else:
    print("Sorry!! Your Subscription has been cancelled")
