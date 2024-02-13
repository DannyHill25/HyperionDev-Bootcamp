#For this task, we need to set up code that has a Logical Error.
#The code that I'm going to write is a program that will ask for certain parameters of a second degree equation.
#With these parameters, we will determine if the equation will have 2, 1 or no real solutions.
#To make this determination, we will establish the cooridnate position of the vertex.
#Based on the 'Y-axis' value, we will determine how many solutions exist for this equation.

#==================================================PSEUDOCODE==================================================#
#Set up the neccessary varaibles
#Ask user to enter the parameters for their equation
#Calculate the coordinates of the Vertex
#Compare the results with respect to the 'Y-axis'
#Print the results based on the comparison result

#=====================================================CODE=====================================================#

import math

print("Welcome! In this program, we will determine how many solutions a second degree equation may have\n")

a = float(input("Please enter the cuadratic coefficient of the equation: "))
while a == 0:
    print("For this to be a Second Degree equation, 'a' must be different than 0\n")
    a = float(input("Please enter the cuadratic coefficient of the equation: "))
b = float(input("Please enter the linear coefficient of the equation: "))
c = float(input("Please enter the constant coefficient of the equation: "))

vertex_y_pos = (c-(pow(b,2))/(4*a))

if vertex_y_pos > 0:
    print('''\nThis equation doesn't have a solution\nThe parabola doesn't cut the X-axis at all''')

elif vertex_y_pos < 0:
    print('''\nThis equation has 2 solutions\nThe parabola cuts the X-axis at 2 points''')

else:
    print('''\nThis equation has 1 solution\nThe parabola is tangent to the X-axis''')

#The only problem with this code, from a logical stand point: it doesn't account for the orientation of the parabola
#If 'a' is a positive number, the parabola is Concave Upwards. The checks performed apply.
#On the other hand, if 'a' is negative, then parabola is Concave Downwards. The logic would be reversed.
#For Vertex > 0, we would have no solution if parabola is Concave Upwards, but 2 if Downwards.
#For Vertex < 0, we would have 2 solutions if Concave Upwards, but no solutions if Downwards.