#Mark Calculation
m1=int(input("Enter your mark in Maths:"))
m2=int(input("Enter your mark in Social:"))
m3=int(input("Enter your mark Science:"))
Total=m1+m2+m3
Avg=Total/3
print("Marks\nMaths:",m1,
      "\nSocial:",m2,"\nSocial:",m3,"\nTotal:",Total,"\nAverage:",Avg)
if(m1>=35 and m2>=35 and m3>=35):
    print("Result:Pass!!")
    if(90<=Avg<=100):
        print("Your Grade is:A")
    elif(80<=Avg<=89):
        print("Your Grade is:B")
    elif(70<=Avg<=79):
        print("Your Grade is:C")
    else:
        print("Your grade is:D")
else:
    print("oops!,You are fail")
