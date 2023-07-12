day=int(input("Enter the date: "))
if(day==0):
    print("Good no fine")
elif(day>=1 and day<=5):
    print("The fine amount is 5")
elif(day>6 and day<=10):
    print("The fine amount is 10")
elif(day>=11 and day<=30):
    print("The fine amount is 15")
else:
    print("the membership expired")
    