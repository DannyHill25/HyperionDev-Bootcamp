#For this task, we need to set up code that will read a string and do 2 things through String Manipulation:
#First instance is to print out the string with each other character being upper case, and the alternative lower case.
#Second instance is to print out the string with each other word being upper case, and the alternative lower case.

#==================================================PSEUDOCODE==================================================#
#Set up the neccessary varaibles
#Ask user to enter a string 
#Change to uppercase every odd character and lower case even characters
#Change every odd placed word in upper case and lower case the even words
#Print the results

#=====================================================CODE=====================================================#

while True:

    user_str = str(input("Please enter a sentence: "))
    str_word_list = user_str.split()                        #List of the words in string
    str_char_mod = ""
    str_word_mod = ""

    for a in range(len(user_str)):                          #Loop through every character in string via index position
        if a % 2 == 0:                                      #Odd index, make character uppercase. Add to variable
            str_char_mod += user_str[a].upper()
        else:                                               #Even index, make character uppercase. Add to variable
            str_char_mod += user_str[a].lower()

    print(str_char_mod)

    for b, word in enumerate(str_word_list):                #Loop through every word in the list via index. Need to enumerate each word in the list
        if b % 2 == 0:                                      #Odd index, make word uppercase in the list
            str_word_list[b]= word.upper()                  
        else:                                               #Even index, make word uppercase in the list
            str_word_list[b] = word.lower()                 
        
    str_word_mod = " ".join(str_word_list)
    print(str_word_mod)