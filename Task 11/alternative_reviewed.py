#For this task, we need to set up code that will read a string and do 2 things through String Manipulation:
#First instance is to print out the string with each other character being upper case, and the alternative lower case.
#Second instance is to print out the string with each other word being upper case, and the alternative lower case.

#=====================================================CODE=====================================================#

while True:

    user_str = str(input("Please enter a sentence: "))
    str_word_list = user_str.split()                        
    str_char_mod = ""
    str_word_mod = ""

    for index in range(len(user_str)):                          
        if index % 2 == 0:                                      
            str_char_mod += user_str[index].upper()
        else:                                               
            str_char_mod += user_str[index].lower()

    print(str_char_mod)

    for position, word in enumerate(str_word_list):                
        if position % 2 == 0:                                      
            str_word_list[position]= word.upper()                  
        else:                                               
            str_word_list[position] = word.lower()                 
        
    str_word_mod = " ".join(str_word_list)
    print(str_word_mod)