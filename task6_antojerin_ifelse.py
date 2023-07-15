'''PF =providant fund DA=dearless allowance MA=medical allowancw'''

designation=input('enter the designation')
if designation=='manager':
   basic_pay=16000
   print('basic_pay',basic_pay)
   allowance =basic_pay*0.12                 
   print('allowance',allowance)
   DA=basic_pay*0.40
   print('DA',DA)
   TA=basic_pay*0.9
   print('TA',TA)
   MA=3000
   LIC=1750
   PF=basic_pay*45
   print('PF=',PF)
elif designation=='team_leader':
    basic_pay=14500
    print('basic_pay',basic_pay)
    allowance=basic_pay*0.9
    print ('allowance',allowance)
    DA=basic_pay*0.37
    print('DA',DA)
    TA=basic_pay*0.6
    print('TA',TA)
    MA=2250
    LIC=1250
    PF=basic_pay*0.37
    print('PF',PF)
elif designation=='Executive':
    basic_pay=10000
    print('basic_pay',basic_pay)
    allowance=basic_pay*0.6
    print('allowance',allowance)
    DA=basic_pay*0.33
    print('DA',DA)
    TA=basic_pay*0.045
    print('TA',TA)
    MA=1800
    LIC=1000
    PF=basic_pay*0.32
    print('PF',PF)
else:
   print('the member is not present')
name_of_employee=input('enter the name')
gross_pay=basic_pay+allowance+DA+TA+MA
print('gross_pay=',gross_pay)
net_pay=gross_pay-(LIC+PF)
print('net_pay',net_pay)


 

