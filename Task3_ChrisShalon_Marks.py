#Program to find whether the student is passed or failed along with there grades .
"""Let m1,m2,m3 be the three marks obtained from the user by prompting"""
m1=int(input("Enter the first mark:"))
m2=int(input("Enter the second mark:"))
m3=int(input("Enter the third mark:"))
"""Total marks will be found by summing up the three marks and the average is found by dividing the total by three"""
total=m1+m2+m3
average=total/3.0
print("The total marks obtained is :",total)
print("The average mark obtained is :",average)
"""Use a nested if statement to find whether the student is passed or failed,along with there grades based upon the marks obtained"""
if(m1>=35 and m2>=35 and m3>=35):
    print("Result:Pass")
    if(average>=90 and average<=100):
        print("Grade:A")
    elif(average>=80 and average<=89):
        print("Grade:B")
    elif(average>=70 and average<=79):
        print("Grade:C")
    else:
        print("Grade:D")
else:
    print("Result:Fail")
    print("No Grade")
