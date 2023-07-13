opening_stock=int(input("Enter the opening stock:"))
purchase=int(input("Enter the purchase:"))
sales=int(input("Enter the sales:"))
print("Opening_stock=",opening_stock,"\nPurchase=",purchase,"\nSales=",sales)
closing_stock=opening_stock+purchase-sales
print("The closing stock=",closing_stock)