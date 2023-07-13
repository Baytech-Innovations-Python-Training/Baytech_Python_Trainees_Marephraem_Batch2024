#checking fine amount for the user getting delay to activate prime membership
print("HOTSTAR""\n""Your Prime Membership is going to expire in certain days Activate your plan to avoid cancellation of prime membership")
n=int(input("Enter the days(plan expired) : "))
if(n==0):
    print("Good no FINE""\n""YOUR PLAN IS ACTIVATED")
elif(n>0 and n<=5):
    print("FINE amount is : ",n*5,"\n""Pay fine amount and activate your plan")
elif(n>5and n<=10):
    print("FINE amount is : ",n*10,"\n""Pay fine amount and activate your plan")
elif (n>10and n<=30):
    print("FINE amount is : ",n*15,"\n""Pay fine amount and activate your plan")
else:
    print("***Your PRIME MEMBERSHIP has been cancelled***")
