#calculating student:mark,avg,grade
m1=int(input("enter a number:"))
m2=int(input("enter a number:"))
m3=int(input("enter a number:"))
total=m1+m2+m3
print(m1+m2+m3)
avg=total/3.0
if(m1>=35 , m2>=35,m3>=35):
    print(" Result:Pass")
if(avg>=90 and avg<=100):
    print("Grade:A")
elif(avg>=80 and avg<=89):
    print("Grade:B")
elif(avg>=70 and avg<=79):
    print("Grade:c")
else:
    print("Grade:D")
if(m1<=35,m2<=35,m3<=35):
    print("Result:fail")
else:
    print( "No Grade")