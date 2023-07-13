#calculating the average marks and determining pass or fail
m1,m2,m3=[int(a) for a in input("Enter the marks m1 m2 m3 : ").split()] # getting input in single line using split()
total=m1+m2+m3
average=total/3.0
print("The total mark is",total)
print("The Average is",average)
if m1>=35 and m2>=35 and m3>=35:
    print("PASS")

    if average>=90 and average<=100:
        print("You got Grade A")
    elif average>=90 and average<=89:
        print("You got grade B")
    elif average >=70 and average <= 79:
        print("You got grade C")
    else:
        print("you got Grade D")
else:
        print("FAIL")
        print("no grade")
