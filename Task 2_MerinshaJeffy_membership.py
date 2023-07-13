#hotstar membership
a=int(input("enter the date: "))
if a==0:
      print("no fine")
elif a<=5:
      print("the fine amount is 5")
elif a<=10:
      print("the fine amount is 10")
elif a<=30:
      print("the fine amount is 15")
elif a>30:
      print("your membership is cancelled")
else:
      print("welcome to join in hotstar membership")
