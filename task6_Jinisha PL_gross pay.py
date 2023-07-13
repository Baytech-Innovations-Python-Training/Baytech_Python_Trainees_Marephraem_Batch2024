basic_pay=150000
name=input("Enter your name: ")
target=int(input("Enter the target you achived: "))
print("Name: ",name)
if(target<100000 and target>0):
    comission=0.15*target
    print("The gross pay is: ",basic_pay+comission)
elif(target>=150000 and target<=250000):
    comission=0.19*target
    print("The gross pay is: ",basic_pay+comission)
elif(target>=250000):
    comission=0.22*target
    print("The gross pay is: ",basic_pay+comission)
else:
    print("No comission.....")

