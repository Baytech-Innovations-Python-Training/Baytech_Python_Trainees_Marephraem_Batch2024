# Calculating a current Bill
Name = (input("Enter the Name:"))
CurentReading = int(input("Enter the CurentReading :"))
PreviousReading = int(input("Enter the PreviousReading:"))
Units = CurentReading - PreviousReading
print("The Units is:", CurentReading - PreviousReading)
if (Units < 500):
    print("The Amount is:", Units * 3 / 4)
elif (Units >= 500 and Units < 1000):
    print("The Amount is:", Units * 5 / 4)
elif (Units >= 1000):
    print("The Amount is", Units * 7 / 4)
else:
    print("Invalid Units")
