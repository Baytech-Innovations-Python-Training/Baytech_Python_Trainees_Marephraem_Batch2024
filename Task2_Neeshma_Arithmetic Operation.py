#Task 1
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
if c==1:
   print(a+b,'Addition')
elif c==2:
    print(a-b,'Subtrction')
elif c==3:
    print(a*b,'Multiply')
elif c==4:
    print(a/b,'Division')
elif c==5:
    print(a%b,'Module')
else:
    print("Invalid input")
