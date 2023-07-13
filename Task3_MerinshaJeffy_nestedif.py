# find the average
m1=int(input("enter the mark"))
m2=int(input("enter the mark"))
m3=int(input("enter the mark"))
total=m1+m2+m3
print(total)
average=total/3
print("the total average is",average)
if m1>=35 and m2>=35 and m3>35:
    print("pass")
    if average>=90<=100:
        print("Grade:A")
    elif average>=80<=89:
        print("Grade:B")
    elif average>=70<=79:
        print("Grade:C")
    elif average<35:
        print("No Grade")
else:
    print("Grade:D")
