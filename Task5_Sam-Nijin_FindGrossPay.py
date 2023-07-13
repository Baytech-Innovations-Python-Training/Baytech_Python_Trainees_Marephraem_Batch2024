basic_pay = 15000

def get_information():

    """ This function accepts no parameter and
        returns the name and target_achieved """
    
    name = input('Enter Employee Name : ')
    target_achieved = float(input('Enter the target value achieved : '))
    return name, target_achieved

name , target_achieved = get_information()

def find_gross_pay(target_achieved, basic_pay):
    if target_achieved <= 100000:
        gross_pay = target_achieved * 15 / 100
        
    elif target_achieved > 100000 and target_achieved < 250000:
        gross_pay = target_achieved * 19 / 100
    
    elif target_achieved > 250000:
        gross_pay = target_achieved * 22 / 100
    return gross_pay + basic_pay

    
if target_achieved > 0:
        gross_pay = find_gross_pay(target_achieved=target_achieved, basic_pay = basic_pay)
        
else:
    print('Enter valid target cost')
    name, target_achieved = get_information()
    gross_pay = find_gross_pay(target_achieved=target_achieved, basic_pay = basic_pay)


print(f'The Employee {name} has a gross pay of {gross_pay}')