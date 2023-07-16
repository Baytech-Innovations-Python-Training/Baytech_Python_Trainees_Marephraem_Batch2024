# Mark Calculation

n1=int(input("Enter the mark : "))
n2=int(input("Enter the mark : "))
n3=int(input("Enter the mark : "))
total=n1+n2+n3
print("The total mark is ",total)
average=total/3.0
print("The average is ",average)

if(n1>=35 and n2>=35 and n3>=35):
    print("Result:Pass")
    if average>=90 and average<=100:
        print("Grade:A")
    elif average>=80 and average<=89:
        print("Grade:B")
    elif average>70 and average<=79:
        print("Grade:C")
    else:
        print("Grade:D")
elif(n1<35 or n2<35 or n3<35):
    print("Result:Fail")
    print("No Grade")