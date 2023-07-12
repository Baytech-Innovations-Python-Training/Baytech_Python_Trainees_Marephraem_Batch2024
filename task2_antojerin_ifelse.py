#calculator
x=int(input('enter the number'))
a=int(input('enter the number'))
b=int(input('enter the number'))
if x==1:
    print (a+b,'adding two numbers')
elif x==2:
    print(a-b,'subracting teo number')
elif x==3:
    print(a*b,'multiplying two number')
elif x==4:
    print(a%b,'dividing two number')
elif x==5:
    print(a/b,'dividing two number')
else:
    print('give number between 1 and 5')
