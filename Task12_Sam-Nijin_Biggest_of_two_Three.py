def biggest_of_two(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2
def biggest_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
        
    elif num2 > num1 and num2 > num3:
        return num2
        
    else:
        return num3

def application():
    print('Welcome to the application')
    print('Choose the function you wanna try out\n1.Biggest of two Values\n2.Biggest of three values')
    choice = int(input('Enter the sl. no. of the operation you need : '))
    match choice:
        case 1:
            num1 = int(input('Enter Value 1 : '))
            num2 = int(input('Enter Value 2 : '))
            result=biggest_of_two(num1=num1, num2=num2)
            return result
            
        case 2:
            num1 = int(input('Enter Value 1 : '))
            num2 = int(input('Enter Value 2 : '))
            num3 = int(input('Enter Value 3 : '))
            result=biggest_of_three(num1=num1, num2=num2, num3=num3)
            return result
        case _:
            return 'Invalid Operation'

result = application()
print(result)