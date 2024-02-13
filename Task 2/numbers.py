#For this task, we will ask the user to provide us with 3 integers and then perform several operations.
#These operations include: sum, subsctraction, multiplication and division.
#The objective is to use the Arithmetic Operations and print out the results.

#Step1: request the 3 integers from the user
int_1 = int(input("Please enter an integer: "))
int_2 = int(input("Please enter an integer: "))
int_3 = int(input("Please enter an integer: "))

#Step2: add all 3 numbers together
sum_int = int_1 + int_2 + int_3
print(sum_int)

#Step3: subtract the second number to the first one
sub_int = int_1 - int_2
print(sub_int)

#Step4: multiply the third number by the first one
mul_int = int_3 * int_1
print(mul_int)

#Step5: divide the sum of all 3 numbers by the third one
div_int = sum_int / int_3
print(div_int)