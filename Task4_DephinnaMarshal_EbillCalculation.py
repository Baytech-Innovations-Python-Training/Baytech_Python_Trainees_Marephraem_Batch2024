#Current Bill CalculationS
Name=input("Enter Your name:")
CReading=float(input("Enter the current Reading:"))
PReading=float(input("Ente the Previous Reading:"))
CConsumption=CReading-PReading
print("Name:",Name)
if CConsumption<500:
    print("The amount to be paid is:",3/4*CConsumption)
elif 500<=CConsumption<1000:
    print("The amount to be paid is:",5/4*CConsumption)
else:
    print("The amount to be paid is:",7/4*CConsumption)

