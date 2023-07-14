#salary calculation based on target achieved

name=input("Enter your name:")
basic_pay=15000
target=int(input("Enter the amount you have achieved:"))

if(target<100000 and target>=0):
    comm=target*15/100
elif(target>=100000 and target<250000):
    comm=target*19/100
elif(target>250000):
    comm=target*22/100
else:
    comm=0

if(comm==0):
    print("You have entered the wrong details!!!!!")
else:
    salary=basic_pay+comm
    print("Name:",name,".Your Gross pay is",salary)