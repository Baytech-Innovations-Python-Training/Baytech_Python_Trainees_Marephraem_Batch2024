current_year = int(input('Enter current Year : '))
join_year = int(input('Enter the year of employment : '))
bonus = 0
if current_year - join_year > 3:
    bonus = 2500
if bonus:
    print(f'Bonus is {bonus}')
else:
    print('No bonus')