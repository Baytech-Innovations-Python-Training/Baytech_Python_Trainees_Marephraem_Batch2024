#total expenses program
quantity=int(input("Enter the Quantity Purchased :"))
amount=int(input("Enter the Amount Per Item :"))
if quantity>10:#if qty>10 the statements executes
    total_expense=quantity*amount
    print("Total Expenses is:",total_expense-total_expense*10/100)#prints it
else:#else if quantity<10
    print("Total Expenses is:",quantity*amount)#prints it
