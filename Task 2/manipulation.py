#For this task, we are going to manipulate a sentence inputted by the user in a variable called 'str_manip'
#Once we have the users sentence, we are going to perform the following tasks:
#1 - Calculate and display the length of 'str_manip'
#2 - Locate the last letter and replace it '@'
#3 - Print the last letter backwards
#4 - Use the first three and last two letters to create a new word

#Step1: get the sentence from the user. Then calculate the length and print it
str_manip = str(input("Please type your sentence here: "))
a = len(str_manip)
print(a)

#Step2: determine the last letter of the sentence and replace it with '@'
last_ch = str_manip[a-1:a]
rpl_str_manip = str_manip.replace(last_ch,"@")
print(rpl_str_manip)

#Step3: print the last 3 characters backwards
last_3_ch = str_manip[a:a-4:-1]
print(last_3_ch)

#Step4: print a 5 letter word with the first 3 and last 2 letters of the sentence
first_3_lt = str_manip[:3]
last_2_lt = str_manip[a-2:a]
print(first_3_lt + last_2_lt)