#descending order using while loop
num=int(input("enter the number of limit"))
x=num
while x>=1:
    print(x,end=" ")
    x-=1
#ascending order using while loop
num=int(input("enter the number of limit"))
x=1
while x<=num:
    print(x,end=" ")
    x+=1
#descending order using for loop
num=int(input("enter the number of limit"))
for i in range(num,0,-1):
    print(i,end=" ")
#ascending order using for loop
num=int(input("enter the number of list"))
for i in range(1,num,+1):
    print(i,end=" ")  
