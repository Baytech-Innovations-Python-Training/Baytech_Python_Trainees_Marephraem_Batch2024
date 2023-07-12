"""
This program is a Python script that prompts the user to enter three marks, then calculates the total and average of those marks,
and then uses if-else statements to determine the result and grade based on the marks.

It starts by using the input() function to ask the user to enter three marks, m1, m2, and m3, which are then stored in variables. 
The program then calculates the total of the marks by adding the three marks and stores it in the variable 'total'
and also calculates the average of the marks by dividing total with 3.0 and stores it in the variable 'average'

Then, the program uses an if-elif block to check the value of the three marks against a series of conditions.
If all three marks are greater than or equal to 35, the program will print "Result : Pass" 
and then again check the average of the marks and calculate the grade If average is greater than or equal to 90 and less than or equal to 100,
the program will print "Grade : A"
If average is greater than or equal to 80 and less than or equal to 89, the program will print "Grade : B" If average is greater than or equal to 70
and less than or equal to 79, the program will print "Grade : C" If none of the above conditions are met, the program will print "Grade : D"
If any of the three marks is less than 35, the program will print "Result : Fail" and "Grade : No Grade"
So the program is checking the student's three marks, calculating the total and average of the marks, and then determining the result and grade based
on the marks and average.


logics
3 Marks as Input
Total
Average
Result
If Pass Grade
    90-100 A
    80-89 B
    70-79 C
    Else D"""




#find marks

m1=int(input("Enter first marks:"))
m2=int(input("Enter second marks:"))
m3=int(input("Enter third marks:"))
total=m1+m2+m3
print("total marks:",total)
average=total/3
print("average:",average)

if(m1>=35 and m2>=35 and m3>=35):
    print("Result:pass")
    if(average>=90 and average<=100):
       print("Grade A")
    elif(average>=80 and average<=89):
       print("Grade B")
    elif(average>=70 and average<=79):
       print("Grade c")
    else:
       print("Grade D")
    
elif(m1<=35 or m2<=35 or m3<=35):
    print("Result:fail")
    print("No grade")
    
