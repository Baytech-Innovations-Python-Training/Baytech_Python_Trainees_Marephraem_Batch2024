#fine program
days=int(input("Enter the days:"))
if days==0:
    print("Good no fine")
elif days>=1 and days<=5:
    print("fine amount:",5)
elif days>5 and days<=10:
    print("fine amount:",10)
elif days>10 and days<=30:
    print("fine amount:",15)
else:
    print("member ship cancel")