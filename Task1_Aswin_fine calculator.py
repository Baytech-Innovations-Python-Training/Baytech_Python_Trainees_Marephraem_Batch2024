#Hotstar bill
#we take number of days late to pay the bill as input
b=int(input("no of days late :"))
#if day is 0 there is no fine 
if b<=0:
    print ( "Good No Fine")
#if day is 1-5 the fine is 5 rs
elif 1<=b and b<=5 :
       print ( "Fine Ammount :",b*5,"Rs" )
#if day is 5-10 the fine is 10 rs
elif 6<=b and b<=10 :
       print ( "Fine Ammount :",b*10,"Rs" )
#if day is 10-30 the fine is 15 rs
elif 11<=b and b<=30 :
       print ( "Fine Ammount :",b*15,"Rs" )
#if day is mor than 30 the membership is canceled
else:
       print ( "Membership Canceled !")
