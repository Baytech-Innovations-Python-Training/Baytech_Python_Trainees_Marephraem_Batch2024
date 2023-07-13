def cal_gross_and_net(bp, hra, da, ta, ma, lic, pf):

    """ This function accepts bp, hra, da, ta, ma, lic,
        pf and returns the gross_pay and net_gross_pay """
    
    gross_pay = bp + hra + da +ta + ma
    net_gross_pay = gross_pay - lic - pf
    
    return gross_pay, net_gross_pay

def calculate_gross_pay(choice):

    """ This function accepts the choice integer as parameter and
        returns the employee_type, gross_pay, bet_gross_pay, bp """
    
    match choice:
    
        case 1:
            employee_type = 'Manager'
            bp = 16000
            hra = bp * 12 / 100
            da = bp * 40 / 100
            ta = bp * 9 / 100
            ma = 3000
            lic = 1750
            pf = bp * 45 / 100
            gross_pay, net_gross_pay = cal_gross_and_net(bp=bp, hra=hra, da=da, ta=ta, ma=ma, lic=lic, pf=pf)
            
        case 2:
            employee_type = 'Team Lead'
            bp = 14500
            hra = bp * 9 / 100
            da = bp * 37 / 100
            ta = bp * 6 / 100
            ma = 2250
            lic = 1250
            pf = bp * 37 / 100
            gross_pay, net_gross_pay = cal_gross_and_net(bp=bp, hra=hra, da=da, ta=ta, ma=ma, lic=lic, pf=pf)

        case 3:
            employee_type = 'Executive'
            bp = 10000
            hra = bp * 6 / 100
            da = bp * 33 / 100
            ta = bp * 4.5 / 100
            ma = 1800
            lic = 1000
            pf = bp * 32 / 100
            gross_pay, net_gross_pay = cal_gross_and_net(bp=bp, hra=hra, da=da, ta=ta, ma=ma, lic=lic, pf=pf)
        case _:
            print('Invalid choice')

    return employee_type, gross_pay, net_gross_pay, bp

print('Choose the designation as follows with th serial number\n')
print('1.Manager\n2.Team Lead\n3. Executive')
choice = int(input('Enter choice : '))

employee_type, gross_pay, net_gross_pay, bp = calculate_gross_pay(choice=choice)

employee_name = input('Enter your name : ')

print(f'{employee_name} is a {employee_type} has a basic pay of Rs.{bp}, gross pay of Rs.{gross_pay} and the net gross pay of Rs.{net_gross_pay}')