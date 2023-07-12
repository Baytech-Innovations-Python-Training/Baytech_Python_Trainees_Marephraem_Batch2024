#Marks
#Average marks
#Total marks
m1=int(input("Enter the mark:"))
m2=int(input("Enter the mark:"))
m3=int(input("Enter the mark:"))
total=m1+m2+m3
print("Total Marks:",total)
average=total/3
print("Average:",average)
if m1>35 and m2>35 and m3>35:
    print("Result:Pass")
    if average>=90 and average<=100:
     print("Grade:A")
    elif average>=80 and average<=89:
     print("Grade:B")
    elif average>=70 and average <=79:
     print("Grade:C")
    else:
     print("Grade:D")
elif m1<35 and m2<35 and m3<35:
    print("Result:Fail")
