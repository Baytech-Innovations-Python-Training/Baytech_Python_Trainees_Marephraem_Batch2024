NAME=input("Enter your name:")
Current_Reading=float(input("Enter the Current Reading="))
Previous_Reading=float(input("Enter the Previous Reading="))
Unit=Current_Reading-Previous_Reading
print(Unit," units has been consumed.")
if Unit<500 :
    print("The amount to be paid by ",NAME,"=",Unit*3/4)
elif Unit>=500 and Unit<1000:
    
    print("The amount to be paid by ",NAME,"=",Unit*5/4)
else :
    print("The amount to be paid by ",NAME,"is",Unit*7/4)