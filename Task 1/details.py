#For this task, we have to request the following information from the user: name, age, house number and street name.
#Once the information is recorded, we have to print a sentence containing all the information collected.
#We will be using the input and print functions to achieve this task.
#First we will set the variables, for which each value will be whatever the users enters in the 'input' functuion.
#Then, we input the 'print' command with the sentence. To input the information in the sentence, we will use {} where
#the information will be placed as empty placed holders. We will use 'str.format()' to insert the information.

#Step1: Collect user information into the variables
name_stg = input("Please enter your name: ")
age_int = input("Please enter your age: ")
num_house_int = input("Please enter your house number: ")
name_street_stg = input("Please enter your street name: ")

#Step2: Set the 'print' sentence using empty placeholders and '.format()' to insert the info collected
print("This is {}, a {} year old resident at {} {}".format(name_stg, age_int, num_house_int, name_street_stg))