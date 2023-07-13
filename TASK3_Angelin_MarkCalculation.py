                        #finding total and average of three marks and also finding the grade

#prompting three numbers
print("                    RESULT")
m1=int(input("enter the mark1:"))
m2=int(input("enter the mark2:"))
m3=int(input("enter the mark3:"))
print("***********************")
print("the mark1 is",m1)
print("the mark2 is",m2)
print("the mark3 is",m3)

#finding total and average
total=m1+m2+m3
average=total/3

#check the condition pass and if pass finding grade
if m1 and m2 and m3>=35:
    print("Result:Pass")
    if average>=90 and average<=100:
      print("Grade A")
    elif average>=80 and average<=89:
        print("Grade B")
    elif average >=70 and average<=79:
        print("Grade C")
    else:
         print("Grade D")
         
#if mark<=35 ,given as fail   
elif m1 and m2 and m3<=35:
    print("Result:fail")
    print("no grade")
print("***********************")

#total mark    
print("the total mark=",total)
#average mark
print("the average mark=",average)
