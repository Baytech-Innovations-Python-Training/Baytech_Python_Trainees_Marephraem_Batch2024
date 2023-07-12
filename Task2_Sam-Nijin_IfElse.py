def calculator():

    """ This function does not accepts any parameters
        Returns the result based on the operation chosen """
    
    is_continue = 1
    while is_continue:
        print('1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Modulo\n')
        choice = int(input('Enter Choice for the above'))
        match choice:
            case 1:
                num1 = int(input('Enter Value 1 : '))
                num2 = int(input('Enter Value 2 : '))
                result = num1 + num2
                # print(result)
            case 2:
                num1 = int(input('Enter Value 1 : '))
                num2 = int(input('Enter Value 2 : '))
                result = num1 - num2
                # print(result)
            case 3:
                num1 = int(input('Enter Value 1 : '))
                num2 = int(input('Enter Value 2 : '))
                result = num1 * num2
                # print(result)
            case 4:
                num1 = int(input('Enter Value 1 : '))
                num2 = int(input('Enter Value 2 : '))
                result = num1 / num2
                # print(result)
            case 5:
                num1 = int(input('Enter Value 1 : '))
                num2 = int(input('Enter Value 2 : '))
                result = num1 % num2
                # print(result)
            case _:
                # print('Invalid Data')
                result = 'Invalid Data'
        print(f'The result is {result}')
        is_continue = int(input('Enter 1 to continue or 0 to stop'))
    return result
        

calculator()