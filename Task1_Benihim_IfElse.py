# Implement a Program to add fine amount if the user forget to pay the membership cost

membership_cost=499
days_left=int(input("The number of days left = "))
if days_left>0 and days_left<=5:
    print("You have to Pay =",membership_cost+days_left*5)
elif days_left>5 and days_left<=30:
    print("You have to Pay =",membership_cost+days_left*15)
elif days_left==0:
    print("You have to pay =",membership_cost)
else :
    print("Subscription Closed")