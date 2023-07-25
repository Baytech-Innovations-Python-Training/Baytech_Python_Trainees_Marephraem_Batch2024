num=int(input("Enter a number :"))
sum=0
number=num
while number>0:
    rem=number%10
    sum=(sum*10)+rem
    number=number//10
if sum==num:
    print ("THE NUMBER IS PALINDROME")
else:
    print ("THE NUMBER IS  NOT A PALINDROME")