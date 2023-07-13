#salary calculation based on target achieved
name=input("enter the name:")
basicpay=15000
targetachieved=float(input("enter the amount:"))
if targetachieved<100000:
    commission=(15/100)*targetachieved
    print(commission)
elif targetachieved>=1.50000 and targetachieved<=2.50000:
    commission=(19/100)*targetachieved
    print(commission)
elif targetachieved>2.50000:
    commission=(22/100)*targetachieved
    print(commission)
grosspay=(basicpay+commission)
print("The grosspay is",grosspay)
