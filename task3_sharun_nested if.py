# finding the total and average of three marks and displaying the grade

m1=int(input("Enter mark1:"))
m2=int(input("Enter mark2:"))
m3=int(input("Enter mark3:"))

total=m1+m2+m3
print("The total marks is",total)

average=total/3
print("The average of your marks is",average)

if(m1>=35 and m2>=35 and m3>=35):
    print("You are passed")
    if(average>=90 and average<=100):
        print("Your grade is A")
    elif(average>=80 and average<=89):
        print("Your grade is B")
    elif(average>=70 and average<=79):
        print("Your grade is C")
    else:
        print("Your grade is D")
else:
    print("You are failed\nGrade: No Grade")



