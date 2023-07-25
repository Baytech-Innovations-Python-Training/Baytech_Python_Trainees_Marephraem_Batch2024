def add(num1, num2):

    """ This function accepts two integer parameter
        and returns the sum of the integer as result """
    
    return num1 + num2

    
def sub(num1, num2):

    """ This function accepts two integer parameter and
        returns the difference between the integers """
    
    return num1 - num2

    
def mul(num1, num2):

    """ This function accepts two integer parameter
            and returns the product of the integer """
    
    return num1 * num2

    
def div(num1, num2):

    """ This function accepts two integer parameter
        and returns the quotient of the integer as result """
    
    return num1 / num2

    
def mod(num1, num2):

    """ This function accepts two integer parameter
        and returns the remainder of the integer as result """
    
    return num1 % num2


def get_value():

    """ This functin accepts no parameters
        and performs prompting two integers
        and returns the promted values """
    
    num1 = int(input('Enter Value 1 : '))
    num2 = int(input('Enter Value 2 : '))
    return num1, num2


def calculator():
    
    """ This function accepts No paramertersfinds
        the arithmetic result as chosen and returns
        the result of the chosen arithmetic operation """
    
    print('1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Modulo\n')
    choice = int(input('Enter Choice for the above'))
    is_continue = 1
    
    while is_continue > 0:
        
        match choice:
        
            case 1:
                num1, num2 = get_value()
                return add(num1=num1, num2=num2)
                
            case 2:
                num1, num2 = get_value()
                return sub(num1=num1, num2=num2)

                
            case 3:                
                num1, num2 = get_value()
                return mul(num1=num1, num2=num2)

            case 4:
                num1, num2 = get_value()
                return div(num1=num1, num2=num2)
                
            case 5:
                num1, num2 = get_value()
                return mod(num1=num1, num2=num2)
                
            case _:
                return 'Invalid Data'
                
        is_continue = int(input('Enter 1 to continue or 0 to stop'))

result = calculator()
print(result)