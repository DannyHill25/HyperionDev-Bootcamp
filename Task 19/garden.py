import spacy
nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "Helen is expecting tomorrow to be a bad day.",
    "The man who hunts ducks out on weekends.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize each sentence in the list and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        print(token, token.orth_, token.orth)
    
    print("Named Entities:")
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
    print("\n")

print(spacy.explain("FAC"))
print(spacy.explain("NORP"))

#Example of two other entities I checked online were CARDINAL and LOC
#CARDINAL - refers to numerical values
#LOC - refers to locations
#I understand CARDINAL, as it is as simple as number that appears in a sentence.
#As for LOC, it's a bit confusing as it is similar to GPE, with the distintion that GPE is "geopolitical";
#it seems like there can be some overlap depending on the word.
#For example, 'beach' is clearly LOC. On the other hand, 'Paris' can fir both entities based on the definition given.