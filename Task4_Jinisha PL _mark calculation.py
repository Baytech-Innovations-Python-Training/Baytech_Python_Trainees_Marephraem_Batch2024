#getting marks from the user and dispalying the result
m1=int(input("Enter mark1: "))
m2=int(input("Enter mark2: "))
m3=int(input("Enter mark 3: "))
total=m1+m2+m3
average=total/3
print("The total mark is: ",total)
print("The average mark is: ",average)
if(m1>=35 and m2>=35 and m3>=35):
    print("Passed")
    if(average>=90 and average<=100):
        print("Grade:A")
    elif(average>=80 and average<=89):
        print("Grade:B")
    elif(average>=70 and average<=79):
        print("Grade:C")
    elif(average>=60 and average<=35):
        print("Grade:D")
    else:
         print("No Grade")
elif(m1<35 and m2<35 and m3<35):
    print("Failed")
else:
     print("No Grade")