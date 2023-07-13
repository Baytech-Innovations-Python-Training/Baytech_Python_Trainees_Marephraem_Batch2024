#stock calculation
opening_stock=int(input("Enter the opening_stock quantity:"))
purchase=int(input("Enter the purchase amount:"))
sales=int(input("Enter the sales amount:"))
closing_stock=opening_stock+purchase-sales
print(closing_stock)
