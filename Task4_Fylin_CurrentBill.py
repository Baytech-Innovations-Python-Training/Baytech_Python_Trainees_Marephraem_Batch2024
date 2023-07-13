# current bill calculation
name=input("Enter your name : ")
x = int(input("Current Reading : "))
y = int(input("Previous Reading : "))
slab=x-y
print("Total Unit is ",slab)
if slab<500:
    print("Customer Name : ", name)
    print ("The amount to be paid is : ",slab * 3/4)
elif slab>=500 and slab<1000:
    print("Customer Name : ", name)
    print("The amount to be paid is : ",slab * 5/4)
elif slab >= 1000:
    print("Customer Name : ", name)
    print("The amount to be paid is : ",slab * 7 / 4)
else:
    print("----Syntax error----")

