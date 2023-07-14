#finding open stock
os=int(input("enter the os:"))
purchase=int(input("enter your purchase:"))
sales=int(input("enter your sales:"))
closingstock=os+purchase-sales
print(closingstock)
