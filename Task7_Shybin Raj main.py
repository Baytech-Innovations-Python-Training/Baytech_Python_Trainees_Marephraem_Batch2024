#closingstock
openingstock=int(input("enter the OS:"))
purchase=int(input("enter the PC:"))
sales=int(input("enter the S:"))
closingstock=openingstock+purchase-sales
print("closingstock",closingstock)