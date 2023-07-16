# To Find Remaining stocks

os=int(input("Enter the Number of Opening Stocks : "))
purchase=int(input("Enter the Number of Stocks Purchased : "))
sales=int(input("Enter the Number of stocks sales : "))
remaining_stocks=os+purchase-sales
print(f"The Remaining Stocks are : {remaining_stocks}")