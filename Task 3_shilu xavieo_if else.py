#calculating the mark
m1=int(input("enter the mark1:"))
m2=int(input("enter the mark2:"))
m3=int(input("enter the mark3:"))
total=m1+m2+m3
average=total/3
print(" total:",total )
print(" average:",average)
if m1>=35 and m2>=35 and m3>=35:
    print("pass")
    if average>=90<=100:
       print("Grade :A")
    elif average>=80<=89:
        print("Grade:B")
    elif average>=70<=79:
        print("Grade:C")
    elif average<35:
        print("no grade")
    else:
        print("grade:d")
else:
    print("fail")
