#Calculating the Fine Amount
n=int(input("Enter the  day:"))
if n==0:
    print("Good no fine")
elif n >= 1 and n <= 5:
     print("Fine Amount:",n*5)
elif n >= 5 and n <= 10:
    print("Fine Amount:",n*10)
elif n >= 15 and n <= 30:
    print("Fine Amount:",n*15)
elif n>30:
    print("Membership cancelled")
