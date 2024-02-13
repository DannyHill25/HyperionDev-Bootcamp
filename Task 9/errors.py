# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #Syntax Error: missing parentheses
print ("\n") #Syntax Error: incorrect indentation and missing parentheses

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" #Syntax Error: unexpected indentation
age = int(age_Str[:2]) #Syntax Error: unexpected indentation / converting string data into integer
print(f"I'm {age} years old.") #Syntax Error: unexpected indentation / concatenating strings and integers

    # Variables declaring additional years and printing the total years of age
years_from_now = "3" #Syntax Error: unexpected indentation
total_years = age + int(years_from_now) #Syntax Error: unexpected indentation / combining string with an integer

print(f"The total number of years:{total_years}") #Syntax Error: missing parentheses / Logical Error: undeclared variable

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = str(total_years * 12 + 6) #Logical Error: missing the 6 extra months for the printed statement
print("In 3 years and 6 months, I'll be " + total_months + " months old") #Syntax Error: unexpected indentation / concatenating strings and integers

#HINT, 330 months is the correct answer