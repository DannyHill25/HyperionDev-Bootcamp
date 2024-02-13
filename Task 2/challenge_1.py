#For this challenge, we are going to calculate the area of a given triangle based on the 3 lengths.
#For this, we will use the formula: square root of (s(s-a)*(s-b)*(s-c)). 's' is half of the sum of all 3 lengths, 
#and 'a', 'b' and 'c' are the lengths of each 
#We will ask the user to provide us the length of the 3 sides, and then we will calculta and print the area

#Step1: enable math modules so we can calculate the square root
import math

#Step2: get the 3 lengths from the user
side1 = float(input("Please provide us with the length of side 1 of the triangle: "))
side2 = float(input("Please provide us with the length of side 2 of the triangle: "))
side3 = float(input("Please provide us with the length of side 3 of the triangle: "))

#Step2: set up the variable 's' of the formula. We will also set up the other parameters of 's' minus the length of each side
s = (side1 + side2 + side3) / 2
a = s - side1
b = s - side2
c = s - side3

#Step3: calculate and print the area of the triangle
area_trg = math.sqrt(s * a * b * c)
print(area_trg)