#salary calculation based on target achived
name=input("enter employee:")
target=int(input("enter your target:"))
basic=15000
if target<100000:
    commission=0.15*target
    print("her commission is: ",commission)
elif target>=100000 and  target<250000:
    commission=0.19*target
    print("her commission is :",commission)
elif target>250000:
    commission=0.22*target
    print("her commission is:",commission)
else:
    print("invalid")
grosspay=basic+commission
print("the gross pay",grosspay)
