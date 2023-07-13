
m1=int(input("ENTER THE ENGLISH MARK="))
m2=int(input("ENTER THE TAMIL MARK="))
m3=int(input("ENTER THE SCIENCE MARK="))
add=m1+m2+m3
average=(add/3)
print("total",add)
print("average",average)
if (m1>=35 and m2>=35 and m3>=35):
    print("result:pass")
    if average>=90 and average>=100:
        print("grade=A")
    elif average>=80 and average>=89:
        print("grage=B")
    elif average>=70 and average>=79:
        print("grade=C")
    else:
        print("grade=D")
        
elif (m1<=35 or m2<=35 or m3<=35):
    print("result:fail")
    print("grade:No Grade")

        
    
