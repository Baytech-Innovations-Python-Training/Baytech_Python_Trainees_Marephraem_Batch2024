days=int(input("enter a day:"))
if(days==0):
    print("good no fine")
elif(days>=1 and days<=5 ):
    print:("fine amount:",days*5)
elif(days>=5 and days<=10):
    print("fine amount:",days*10)      
elif(days>=10 and days<=30):
     print("fine amount:",days*15)   
else:
    print("membership canceled")     