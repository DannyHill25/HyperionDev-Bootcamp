#For this challenge, we have to request the user's favourite restaurant and number.
#We will then store these in variables as Data Types 'string' and 'integer' respectively.
#Both should be printed in 2 different statements, and then cast the number as a string and attempt to print it.

#Step1: request the user's favourite restaurant and number. Store the name as a 'string' and the number as an 'integer'
string_fav = str(input("Please enter your favourite restaurant: "))
fav_num = input("Please enter your favourite number: ")
int_fav = int(fav_num)

#Step2: print each variable in two different statements
print(string_fav)
print(int_fav)

#Step3: cast 'string_fav' as an 'integer'
string_fav = int(string_fav)

#When running the code, when we reach the casting phase of 'string_fav' into an 'integer' we get a "ValueError" message.
#This is due to the fact that we are attempting to cast a non-valid DataType into another.
#'integers' are for numbers (with no decimal places), so when attempting to cast a non-numeric characters,
#you run into this ValueError. To cast a 'string' into an 'integer', the string has to contain only numeric characters.