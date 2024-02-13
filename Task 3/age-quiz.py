#For this task, we need to create a program that output a specific message based on the age inputted.
#Request user to enter their age
#If age is 40 or over, print "You're over the hill"
#For ages over 100, print "Sorry, you're dead"
#If age is 65 or older, print "Enjoy your retirement"
#If user is 13 or younger, print "You qualify for the kiddie discount"
#If user is exactly 21, print "Congrats on your 21st!"
#For any other age, print "Age is but a number"

age = int(input("Please enter your age here: "))
age_21 = False #setting logical test for age 21 case

if age == 21: #Change boolean value if user enters 21
    age_21 = True

if age_21: 
    print("Congrats on your 21st!") #Code ends in the 21 case. If false, continue with other checks
else:
    if age <=13:
        print("You qualify for the kiddie discount")
    elif (40 <= age < 65):
        print("You're over the hill")
    elif (65 <= age < 100):
        print("Enjoy your retirement")
    elif (age >= 100):
        print("Sorry, you're dead")
    else:
        print("Age is but a number")
