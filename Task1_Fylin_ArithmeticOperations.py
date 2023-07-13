#getting 2 numbers from user and doing the operation which we defined
x,y=[int(a)for a in input("Enter two numbers : ").split()]
print("WE HAVE SEVERAL OPERATIONS")
print("1.Addition""\n""2.Subtraction""\n""3.Multiplication""\n""4.Division""\n""5.Modulo")
n=int(input("Choose the operation by entering no. : ")) #promting user to select number
if (n==1): #checking the variale n is assigned with value 1 or not
    print("The Addition of those numbers is",x+y)
elif (n==2):
    print("The Subtraction of those numbers is",x-y)
elif (n==3):
    print("The Multiplication of those numbers is",x*y)
elif (n==4):
    print("The Division of those numbers is",x/y)
elif (n==5):
    print("The Modulo of those numbers is",x%y)
else:
    print("***Invalid choice***")


