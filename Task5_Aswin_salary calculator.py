#salary calculator
#getting employee name as input
name=(input("Enter Employee Name :"))
#the basic pay is given
basic=15000.0
#getting input of target the employee reached
target=int(input("Enter the Reached Target Ammount :"))
"""if the target is below 100000 the system print salary based
on the commision they earnd"""
if target<100000:
    print ("The Gross Pay for",name,"is :",basic+target*15/100,"Rs.")
"""if the target is between 100000 - 250000 the system print salary based
on the commision they earnd"""
elif target>100000 and target<250000 :
    print ("The Gross Pay for",name,"is :",basic+target*19/100,"Rs.")
"""else the target is above 250000 the system print salary based
on the commision they earnd"""
else:
        print ("The Gross Pay for",name,"is :",basic+target*22/100,"Rs.")
