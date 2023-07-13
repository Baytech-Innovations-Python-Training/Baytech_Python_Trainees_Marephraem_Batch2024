# task1
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
>30     Membership Cancel """
a=int(input("enter the days you are paid="))
if a==0:
    print("no fine")
elif a<=5:
    print(" fine amound=5$ fine" ,a*5)  
elif a<=10:
    print(" fine amound=10$ is fine",a*10)
elif a<=30:
    print("fine amound=15$ is fine",a*15 )
else:
    print("member ship cancel")



























