# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #Syntax Error: missing " "
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" #This line contains 2 errors:
#Syntax Error: missing '.format' to add the value of the variables
#Logical Error: 'animal_type' and 'number_of_teeth' are in the wrong order

print(full_spec) #Syntax Error: missing parenthesis