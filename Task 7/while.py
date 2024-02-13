#For this task, we need to set up a loop requesting numbers from the user.
#Once the user inputs '-1', the loop stops and the program returns the average of all numbers recorded.

#==================================================PSEUDOCODE==================================================#
#Set up the neccessary varaibles
#Request user to input a number
#Check that this first number is different than '-1'
#If first input is '-1', ask user to input a different number
#Use While loop to ask for different number, adding to the loop count and sum of all numbers
#Once user inputs '-1', exit loop and print calculated average


#=====================================================CODE=====================================================#

i = 0
sum = 0
num = int(input("Please enter a number: "))

while num == -1:
    print("Sorry, the first number can't be -1\n")
    num = int(input("Please enter a number other than -1: "))

while num != -1:
    i += 1
    sum += num
    num = int(input("\nPlease enter another number: "))

sum_ave = round(float(sum/i),2)
print("\nThe average of all input numbers is {}".format(sum_ave))