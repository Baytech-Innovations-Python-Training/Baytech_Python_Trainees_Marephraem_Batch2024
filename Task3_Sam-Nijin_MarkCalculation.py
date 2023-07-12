m1 = int(input('Enter mark of sub 1'))
m2 = int(input('Enter mark of sub 2'))
m3 = int(input('Enter mark of sub 3'))

def total(m1, m2, m3):
    
    """ This function accepts 3 subject value
        and returns the total value of subjects """
    
    return m1 + m2 + m3
    
total = total(m1=m1, m2=m2, m3=m3)
print(f'Total is {total}')

def avg(total):

    """ This function accepts total as parameter
        and returns the average value for total """
    
    return total / 3.0
    
average = avg(total=total)
print(f'Average is {average}')

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print('Result: Pass')
    if average >= 90 and average <= 100:
        print('Grade : A')
    elif average >= 80 and average <= 89:
        print('Grade : B')
    elif average >= 70 and average <= 79:
        print('Grade : C')
    else:
        print('Grade : D')
    
elif m1 < 35 or m2 < 35 or m3 < 35:
    print('Result: Fail')
    print('Grade : No Grade')