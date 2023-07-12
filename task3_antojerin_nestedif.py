#report card grading
m1=int(input('enter the mark'))
m2=int(input('enter the mark'))
m3=int(input('enter the mark'))
'''print('m1,m2,m3')'''
total=m1+m2+m3
print('total=',total)
average=total/3
print('average=',total/3)
if m1>=35 and m2>=35 and m3>=35:
    print('pass')
    if average>=90:
        print("grade is A")
    elif average>=80 and average<=89:
        print ('grade is B')
    elif average>=70 and average<=79:
        print('grade is C')
    else:
        print('grade is D')
else:
    print('fail \ngrade:no grade')
        

