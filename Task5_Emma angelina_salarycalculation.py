Basic_pay=15000
NAME=input("Enter your Name:")
Target_acheived=float(input("Enter the target acheived:"))
if Target_acheived<100000:
    print("Gross pay of ",NAME,"=",Basic_pay+Target_acheived*15/100)
elif Target_acheived>=100000 and Target_acheived<250000:
    print("Gross pay of ",NAME,"=",Basic_pay+Target_acheived*19/100)
else:
    print("Gross pay of ",NAME,"=",Basic_pay+Target_acheived*22/100)
    
