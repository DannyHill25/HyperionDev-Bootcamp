#For this task, we need to set up a loop to print a patern of stars.
#We are only allowed to use a single 'for loop' and one 'if-else' statement to make it.

#==================================================PSEUDOCODE==================================================#
#Set up the neccessary varaibles
#Set up the 'for loop' to print out the pattern
#Using 'if-else' we will do the following:
#While count is less than or equal to '5', add a star
#Once count is greater than '5', remove a star
#Print out the correspondant '*' every iteration

#=====================================================CODE=====================================================#

stars = ""

for i in range(1, 10):
    if i <= 5:
        stars += "*"
        print(stars)
    else:
        stars = stars[:-1]
        print(stars)