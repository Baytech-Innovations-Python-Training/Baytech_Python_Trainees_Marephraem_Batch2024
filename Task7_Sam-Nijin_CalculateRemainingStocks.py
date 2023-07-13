def rem_stocks(os, purchase, sales):

    """ This function accepts three parameters
        as count of os, purchage, sales and 
        returns the count of the closing stock """

    return os + purchase - sales


os = int(input('Enter Number of opening stocks : '))
purchase = int(input('Enter number of stocks purchased : '))
sales = int(input('Enter number of stocks sales : '))

remaining_stocks = rem_stocks(os=os, purchase=purchase, sales=sales)
remaining_stocks