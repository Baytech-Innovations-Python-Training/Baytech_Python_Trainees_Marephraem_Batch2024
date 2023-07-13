#current bill
name=input("enter the name:")
pervious=int(input("enter the values"))
current=int(input("enter the values"))
b=(name+" current charge is ")
a=pervious-current
x=3/4*a
y=5/4*a
z=7/4*a
print(a)
if a>500:
    print(b,x)
elif a<=500>1000:
    print(b,y)
elif a<=10000:
    print(b,z)
else:
    print("no amount")
    
