OpeningStock=int(input("Enter the opening stock:"))
Purchase=int(input("Enter the Purchase:"))
Sales=int(input("Enter the sales:"))
ClosingStock=OpeningStock+Purchase-Sales
print("Opening Stock:",OpeningStock,"\nPurchase:",Purchase,"\nSales:",Sales,"\nClosing Stock:",ClosingStock)
