BasicPay=15000
Name=input("Enter Your Name:")
Target=float(input("Enter the target achieverd by you:"))
print("Name:",Name)
if Target<100000:
    print("The commision for",Name,"is",(15/100)*Target,"\nGross pay is:",BasicPay+(15/100)*Target)
elif 100000<=Target<=250000:
    print("The commision for",Name,"is",(19/100)*Target,"\nGross pay is:",BasicPay+(19/100)*Target)
else:
    print("The commision for",Name,"is",(22/100)*Target,"\nGross pay is:",BasicPay+(22/100)*Target)
