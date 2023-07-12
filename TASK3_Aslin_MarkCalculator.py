#mark calculator
      
   #mark
m1=int(input("enter the number:"))
m2=int(input("enter the number:"))
m3=int(input("enter the number:"))
total=m1+m2+m3
print("total:",total)
average=total/3
print("average:",average)
if(m1>=35 and m2>=35 and m3>=35):
     print("Result:pass")
     if (average>=90 and average<=100):
      print("Grade:'A'")
     elif(average>80 and average<=89):
      print("Grade:'B'")
     elif(average>70 and average<=79):
      print("Grade:'c'")
     else:
      print("Grade:'D'")       
elif(m1 and m2 and m3<35):
     print("Result:fail")
     
