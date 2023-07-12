#prompting marks from the users
MARK_1=int(input("ENTER THE MARK 1="))
MARK_2=int(input("ENTER THE MARK 2="))
MARK_3=int(input("ENTER THE MARK 3="))
Total=MARK_1+MARK_2+MARK_3
AVERAGE=Total/3
print("Total mark=",Total,"/300")
if MARK_1>=35 and MARK_2>=35 and MARK_3>=35:
    print("Congrats!! you are passed!")
    print("AVERAGE=",AVERAGE)
    if AVERAGE>=90 and AVERAGE<=100:
        print("Your Grade :A")
    elif AVERAGE>=80 and AVERAGE<=89:
         print("Your Grade :B")
    elif AVERAGE>=70 and AVERAGE<=79:
         print("Your Grade :C")
    else:
         print("Your Grade:D")
else:
     print("SORRY!!YOU ARE FAILED....BEST LUCK NEXT TIME!!")