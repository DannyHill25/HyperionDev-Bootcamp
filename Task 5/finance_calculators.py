#First Capstone of the bootcamp. Objective: write code on a calculator that determines the profits of an investment
#based on if it is am 'investment or 'bond'. If 'investment' is selected, it will deternime 'simple' or 'compound'
#interest based on what the user specifies in the 'investment' calculation

#==================================================PSEUDOCODE==================================================#
#Present user with calculation option: 'investment' and 'bond'
#Request user to declare their calculation type
#If user inputs something outside of 'investment' or 'bond', display error message
#If 'investment' is chosen, request 'deposit amount', 'interest rate' and 'years of investment'
#Request if they want 'simple' or 'compound' interest. Print the results
#If 'bond' is selected, request 'house value', 'interest rate' and 'months'
#Print the results

#=====================================================CODE=====================================================#
import math

print('''Thank you for using this Financial Calculator. You will have the option to calculate two products
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan''')

calc_select = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

if calc_select == "investment":
    inv_amount = float(input("Please enter the investment amount: "))
    inv_int_rate = float(input("Please enter the interest rate(without the '%'): "))
    inv_time = float(input("Please enter the years of investment: "))
    interest = str(input("Please select the investment type - 'simple' or 'compound': ")).lower()

    if interest == "simple":
        total_int = round(inv_amount*(1 + inv_int_rate*inv_time),2)
        print("Your simple interest from this invest would be {}".format(total_int))

    elif interest == "compound":
        total_int = round(inv_amount*math.pow((1+inv_int_rate),inv_time),2)
        print("Your compound interest from this invest would be {}".format(total_int))

elif calc_select == "bond":
    bond_house_value = float(input("Please enter the value of the house: "))
    bond_int_rate = float(input("Please enter the interest rate(without the '%'): "))
    bond_time = float(input("Please enter how many months you will take for the repayment: "))
    total_bond = round((bond_int_rate*bond_house_value)/(1-(1 + bond_int_rate)**(-bond_time)),2)
    print("Your monthly repayment would be {}".format(total_bond))

else:
    print("Sorry, you have not chosen one of the two calculations offered")