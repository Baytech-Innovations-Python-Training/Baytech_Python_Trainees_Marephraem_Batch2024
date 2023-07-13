
m1=int(input("Enter the value"))
m2=int(input("Enter the value"))
m3=int(input("Enter the value"))
total=m1+m2+m3
average=(m1+m2+m3)/3.0
if(m1>=35 and m2>=35 and m3>=35):
    print("Result:pass")
if(average>=90 and average<=100):
    print("Grade A")
elif(average>=80 and average<=89):
    print("Grade B")
elif(average>=70 and average<=79):
    print("Grade c")
    else(average<70):
      print("Grade D")
else (m1<35 and m2<35 and m3<35):
    print("No GRade")
    print("fail")
