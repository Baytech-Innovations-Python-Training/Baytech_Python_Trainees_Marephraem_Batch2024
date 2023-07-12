#current bill
user_name='anto jerin'
current_reading =int(input('enter the reading'))
previous_reading=int(input('enter the reading'))
total_number_of_unit_of_current_consumption=current_reading-previous_reading
print('total_number_of_unit_of_current_consumption=',total_number_of_unit_of_current_consumption)
if total_number_of_unit_of_current_consumption<500:
    print('current charge=',total_number_of_unit_of_current_consumption*(3/4))
elif total_number_of_unit_of_current_consumption<1000:
    print('current charge=',total_number_of_unit_of_current_consumption*(5/4))
else:
    print('current charge=',total_number_of_unit_of_current_consumption*(7/4))
    print('user_name=',user_name)
