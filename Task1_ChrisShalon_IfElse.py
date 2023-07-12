#Program to check the fine amount based upon the days
"""Get the date from the user by prompting"""
Day=int(input("Enter the Day:"))
if(Day==0):#If the user pays the amount before the due date then the user will not be fined
    print("Good No Fine")
elif(Day>=1 and Day<=5):#If the user pays the amount inbetween 1-5 days,then the user will be fined by 5rs
    print("Fine amount :",Day*5)
elif(Day>5 and  Day<=10):#If the user pays the amount inbetween 6-10 days,then the user will be fined by 10rs
    print("Fine amount :",Day*10)
elif(Day>10 and Day<=30):#If the user pays the amount inbetween 11-30 days,then the user will be fined by 15rs
    print("Fine amount:",Day*15)
else:#If the user did not pay the amount after 30 days the users membership is canceled
    print("Membership canceled")
