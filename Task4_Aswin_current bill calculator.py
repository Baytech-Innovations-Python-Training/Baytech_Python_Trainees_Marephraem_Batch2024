#current bill calculator
#getting the name as input
name=(input("Enter Your Name :"))
#input the Current Reading
c=int(input("Enter the Current Reading :"))
#input the Previous Reading
p=int(input("Enter the Previous Reading :"))
#cc is the difference between the current and previous reading
cc=c-p
#printing the cc value
print ("The Current Consumption is :",cc,"Units")
#if the cc is below 500 the system print current bill with name
if cc<500:
    print ("The current Bill for",name,"is :",cc*3/4)
#if the cc is between 500-1000 the system print current bill with name
elif cc>=500 and cc<1000:
        print ("The current Bill for",name,"is :",cc*5/4)
#if the cc is above 1000 the system print current bill with name
elif cc>=1000:
        print ("The current Bill for",name,"is :",cc*7/4)
#if input is invalid it prints server error
else:
        print ("sever error")

