#to find total average and grade using if condition:
m1=int(input("Enter the mark:"))
m2=int(input("Enter the mark:"))
m3=int(input("Enter the mark:"))
total=m1+m2+m3
avg=m1+m2+m3/3.0
print("Total:",total)
print("Avg:",avg)
if(m1>=35 and m2>=35 and m3>=35):
    print("Result:Pass")
    if(avg>=90 and avg<=100):
        print("Grade:A")
    elif(avg>=80 and avg<=89):
        print("Grade:B")
    elif(avg>=70 and avg<=79):
        print("Grade:C")
    else:
        print("Grade:D")
elif (m1<35 and m2<35 and m3<35):
    print("No grade")
    print("Fail")