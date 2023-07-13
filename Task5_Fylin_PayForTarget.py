#salary calculation based on target achieved
Name=input("Enter your Name (to calculate salary) : ")
BasicPay=15000
T=int(input("Enter your Target : "))
if T<100000 and T>0:
    commission=T*15/100
elif T>=100000 and T<250000:
    commission=T*19/100
else:
    commission=T*22/100

GrossPay=BasicPay+commission
print("Gross pay : ",GrossPay)

print("\n","Employee name :",Name,"\n","SALARY : ",GrossPay)

