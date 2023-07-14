name=input("enter the name=")
target=int(input("enter the target amount="))
basicpayment=15000
if target<=100000:
    commission=0.15*target
    print("her commission",commission)
elif target>=100000 and target<250000:
    commission=0.19*target
    print("her commission",commission)
elif target>=250000:
    commission=0.22
    print("her commission",commission)
grosspay=(basicpayment+commission)
print("the gross payment is=",grosspay)

