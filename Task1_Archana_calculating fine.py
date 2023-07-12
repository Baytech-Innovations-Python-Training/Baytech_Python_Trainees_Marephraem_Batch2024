"""
This program is checking the number of days and based on the number of days it is calculating the fine.

Assume that you are having a Prime Hotstar Membership and its going to expire in certain Days, 

If you are paying the amount on the End Date you have no fine (0 days no fine ) , your output should be
print("Good No Fine")

If you are paying the amount inbetween 1-5 days you have 5rs as fine(1-5 days 5rs fine) , your output should be
print("Fine Amount : ",(amount should be printed here))

If you are paying the amount inbetween 5-10 days you have 15rs as fine(5-10 days 5rs fine) , your output should be
print("Fine Amount : ",(amount should be printed here))

If you are paying the amount inbetween 10-30 days you have 15rs as fine(10-30 days 15rs fine) , your output should be
print("Fine Amount : ",(amount should be printed here))

If the amount is not paid more than 30 days 
print("Membership Cancel")

 elif Statement in Python
"""
"""
0       No Fine
1-5     5
5-10    10
10-30   15
>30     Membership Cancel """






#calculating fine
days=(int(input("Enter the days")))
if(days==0):
    print("Good No fine")
elif(days>=1 and days<=5):
    print("fine amount:",days*5)
elif(days>=5 and days<=10):
    print("fine amount:",days*10)
elif(days>=10 and days<=30):
    print("fine amount:",days*15)
elif(days>30):
    print("Membership cancel")




