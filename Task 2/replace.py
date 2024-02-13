#For this task, we are going to manipulate a 'string' using the functions 'replace' and 'upper',
#and using slicing to reverse the sentence
#We will store the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog." as our baseline.
#We will then use 'replace' to remove the "!", after that we will convert all characters to upper case, 
#and finally reverse the entire sentence.

#Step1: Set the baseline sentence
sent = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sent)

#Step2: Remove the "!"
sent_replaced = sent.replace("!"," ")
print(sent_replaced)

#Step3: Make all characters upper case
sent_upper = sent_replaced.upper()
print(sent_upper)

#Step4: Reverse the entire sentence
sent_reversed = sent_upper[::-1]
print(sent_reversed)