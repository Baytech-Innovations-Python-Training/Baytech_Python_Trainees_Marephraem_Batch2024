"""Calculating the closing stock"""
opening_stock=int(input("Enter the opening stock:"))
purchased=int(input("Enter the stock purchased:"))
print("The total number of stock:",opening_stock+purchased)
sales=int(input("Enter the number of sales:"))
#closing stock
closing_stock=(opening_stock+purchased)-sales
print("The Closing Stock is:",closing_stock)