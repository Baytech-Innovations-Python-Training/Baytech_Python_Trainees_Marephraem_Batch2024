"""prompting the marks from the user and displaying whether user is pass or not"""
m1=int(input("Enter the mark1:"))#prompting the mark as input
m2=int(input("Enter the mark2:"))
m3=int(input("Enter the mark3:"))
total=m1+m2+m3  #finding the total
average=total/3.0  #finding the average
print("your total mark(mark1+mark2+mark3)=",total)
print("Your average mark=",average)
if(m1>=35 and m2>=35 and m3>=35):
    print("Passed..")
    if(average<=100 and average>=90):
        print("GRADE: A")
    elif(average<=89 and average>=80):
        print("GRADE: B")
    elif(average<=79 and average>=70):
        print("GRADE: C")
    elif(average<=69 and average>=35):
        print("GRADE: D")
    else:
        print("No grade...")
else:
    print("Failed... \n Try hard")
