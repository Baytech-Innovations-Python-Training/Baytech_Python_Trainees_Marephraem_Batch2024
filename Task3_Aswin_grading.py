#Grading
#input mark 1 as m1
m1=int(input("Enter the mark m1 :"))
#input mark 2 as m2
m2=int(input("Enter the mark m2 :"))
#input mark 3 as m3
m3=int(input("Enter the mark m3 :"))
#total mark is calculated by adding the three input marks
Total=m1+m2+m3
#average mark is calculated
Average=Total/3.0
#printing the total mark
print ("Total Marks=",Total,"/300")
#printing the average mark
print ("Averag=",Average)
#if the all the mark is above 35 the result is pass
if m1>=35 and m2>=35 and m3>=35:
    print ("Result : PASS")
#if the average mark is between 90-100 the grade is A
    if Average>=90 and Average<=100:
        print ("Grade : A")
#if the average mark is between 80-89 the grade is B   
    elif Average>=80 and Average<=89:
        print ("Grade : B")   
#if the average mark is between 70-79 the grade is C
    elif Average>=70 and Average<=79:
        print ("Grade : C")
#if the average mark is below 70 the grade is D
    else:
        print ("Grade : D")
"""if any one of the the mark is below 35
the result is fail and they have no grade"""
else:
    print ("Result : FAIL")
    print ("Grade : No Grade")
