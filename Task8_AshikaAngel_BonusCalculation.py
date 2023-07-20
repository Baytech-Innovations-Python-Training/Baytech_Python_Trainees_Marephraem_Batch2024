"""Calculating Bonus"""
name=input("Enter your name:")
current_year=int(input("Enter the current year:"))
joined_year=int(input("Enter the joined year:"))
print("Name:",name)
experience=current_year-joined_year
if(experience>3):
    print("Your Bonus is 2500 RS")
else:
    print("No Bonus..")    