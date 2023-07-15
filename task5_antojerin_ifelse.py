
target_achieved=int(input('enter the target'))
basic_pay=15000
if target_achieved<100000 :
    com=target_achieved*0.15
    print('com=',target_achieved*0.15)
elif target_achieved >=100000 and target_achieved<=250000:
    com=target_achieved*0.19
    print ('com=',target_achieved*0.19)
elif target_achieved>=250000:    
    com=target_achieved*0.22
    print ('com=',target_achieved*0.22)
user_name='anto jerin'
print('user_name=',user_name)
gross_pay=basic_pay+com
print('gross_pay=',gross_pay)
