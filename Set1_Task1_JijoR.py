#Profit loss Program in Python
cost_price=float(input("Enter the cost price of an item:"))
selling_price=float(input("Enter the selling price of an item:"))
if selling_price>cost_price:
    profit=selling_price-cost_price
    print("The profit is:",profit)
elif cost_price>selling_price:
    loss=cost_price-selling_price
    print("The loss is:",loss)
else:
    print("No profit No loss")
