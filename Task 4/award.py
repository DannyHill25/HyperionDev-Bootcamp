#For this task, we need to determine the award that the user will recieve based on their time in the 3 phases of a triathlon.
#Ask user to enter their swimming time
#Ask user to enter their cycling time
#Ask user to enter their running time
#Calculate and display the total time
#Determine the award based on their total time

swim_time = int(input("Please enter your swimming time in minutes: "))
cycle_time = int(input("Please enter your cycling time in minutes: "))
run_time = int(input("Please enter your running time in minutes: "))
triathlon_time = swim_time + cycle_time + run_time
results = f"Your total time in the Triathlon was {triathlon_time} minutes"
print(results)
award = "No award unfortunately" #Setting default award
if award == "No award unfortunately" and triathlon_time >= 111:
    print(award)
elif 106 <= triathlon_time < 111:
    award = "Provincial Scroll"
    award_prtn = f"Congratulations on your {award}!"
    print(award_prtn)
elif 100 < triathlon_time <= 105:
    award = "Provincial Half Colour"
    award_prtn = f"Congratulations on your {award}!"
    print(award_prtn)
else:
    award = "Provincial Colour"
    award_prtn = f"Congratulations on your {award}!"
    print(award_prtn)