Num=int(input("Enter the Number :"))
Sum=0
temp=Num  #Assigning the value in a temporary variant
while Num>0 :
    Rem=Num%10    #Dividing by 10 to extract last digit
    Sum=(Sum*10)+Rem
    Num=Num//10
if(Sum==temp):
    print(temp," is palindromic Number!!")
else:
    print(temp, " is not Palindromic number.")
