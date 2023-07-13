#Program to find the closing stock
Opening_stock=int(input("Enter the Opening Stock:"))
Purchase=int(input("Enter the no of purchased items:"))
Sales=int(input("Enter the no of sold items:"))
Closing_stock=Opening_stock+Purchase-Sales
print("Closing_stock",Closing_stock)   
