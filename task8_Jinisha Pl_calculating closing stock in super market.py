opening_stock=int(input("Enter the opening stock: "))
purchase_stock=int(input("Enter the purchase: "))
sales=int(input("Total sale: "))
closing_stock=(opening_stock+purchase_stock)-sales
print("The closing stock is: ",closing_stock)