#Calculating the Marks
m1=int(input("Enter the number:"))
m2=int(input("Enter the number:"))
m3=int(input("Enter the number:"))
Total=m1+m2+m3
print("Total_mark:",m1+m2+m3)
Average=Total/3
print("Average_mark:",Total/3)
if m1>35 and m2>35 and m3>35:
    print("The result is Pass")
    if(Average>=90 and Average<=100):
        print("Grade is A")
    elif (Average >= 80 and Average <= 89):
        print("Grade is B")
    elif (Average >= 70 and Average <= 79):
        print("Grade is C")
    else:
        print("Grade is D")
elif m1<35 and m2<35 and m3<35:
    print("The result is Fail")