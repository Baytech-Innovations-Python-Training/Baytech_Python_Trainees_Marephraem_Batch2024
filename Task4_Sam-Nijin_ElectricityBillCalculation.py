current_reading = float(input('Enter your current reading : '))
previous_reading = float(input('Enter your previous reading : '))
name = input('Enter your name : ')
current_consumption = current_reading - previous_reading

print('\n********** Billing Information **********\n')
print(f'The user Name is : {name}')
print(f'The units used is {current_consumption}')

if current_consumption <= 500:
    print(f'The bill is {current_consumption * 3/4}')
elif current_consumption > 500 and current_consumption <= 1000:
    print(f'The bill is {current_consumption * 5/4}')
else:
    print(f'The bill is {current_consumption * 7/4}')