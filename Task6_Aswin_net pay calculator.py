#net pay calculator
#getting name and designation as input
name=(input("Employee Name :"))
des=(input("Employee Designation :"))
#the salary is calculated based on the allowence for each designation
"""if the designation is manager
it calculate the salary using the conditions below""" 
if des =="manager":
    bp = 16000
    hr = bp*12/100
    da = bp*40/100
    ta = bp*9/100
    pf = bp*45/100
    ma = 3000
    lic = 1750
"""if the designation is team leader
it calculate the salary using the conditions below"""
elif des =="team leader" :
    bp = 14500
    hr = bp*9/100
    da = bp*37/100
    ta = bp*6/100
    pf = bp*37/100
    ma = 2250
"""if the designation is executive
   it calculate the salary using the conditions below"""    
elif des =="executive" :
    bp = 10000
    hr = bp*6/100
    da = bp*33/100
    ta = bp*4.5/100
    pf = bp*32/100
    ma = 1800
    lic = 1000    
#if somebody enter invalid input it consider all values as zero
else:
    bp = 0
    hr = 0
    da = 0
    ta = 0
    pf = 0
    ma = 0
    lic = 0    
#calculating the gross pay  
gp=bp+hr+da+ta+ma
#calculating the net pay
np=gp-pf+lic
"""if somebody enter invalid input it consider all values as zero
   and if the gross pay and net pay is zero the system asks the user
   to enter valid data"""
if gp==0 and np==0:
    print ("enter valid data !")
#else the system print the net pay and gross pay with designation and employee name    
else:
    print ("Employee Name :",name)
    print ("Employee Designation :",des)
    print ("Basic Pay:",bp,"Rs.")
    print ("Gross Pay :",gp,"Rs.")
    print ("Net Pay :",np,"Rs.")
