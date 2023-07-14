  #calculating closing stock based on opening stock,purchase and sales

#prompting openng stock
opening_stock=int(input("enter the opening stock amount:"))

#prompting purchase
purchase=int(input("enter the purchase:"))

#prompting sales
sales=int(input("enter the sales:"))

#calculating closing stock
closing_stock=opening_stock+purchase-sales

#printing the result
print("***************************")
print("todays opening_stock is:",opening_stock)
print("todays purchase is:",purchase)
print("todays sales is:",sales)
print("todays closing stock is given by:",closing_stock)
print("***************************")
