import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2)) #Results - 0.5929930274321619
print(word3.similarity(word2)) #Results - 0.40415016164997786
print(word3.similarity(word1)) #Results - 0.22358825939615987

#Based on these results, the 60% similarity between 'cat' and 'monkey' has to be becasue they are both animals
#When comparing 'banana' to the other two, they are clear less similar as it's a fruit agaisnt an animal; the interesting
#part comes with the 18% difference, mainly due to the fact that 'monkey' also has 6 characters, and 'monkey' and 
#'banana' do have a stronger link than 'cat' and 'banana'

word4 = nlp("orange")
word5 = nlp("tiger")
word6 = nlp("lion")

print(word4.similarity(word5)) #Results - 0.23944314262404284
print(word6.similarity(word4)) #Results - 0.15005961787582137
print(word6.similarity(word5)) #Results - 0.7136095195259959

#Was testing if may the fact that a 'tiger' has some 'orange' in it's fur would give it a stronger relationship; not as much as I
#rationalised, but still much stronger than with 'lion'. Compared to the previous two animals, my example shows a much stronger
#similatiry, as both are from the feliny family

#--------------------'md' VS 'sm' comparison--------------------#

#When running the example file with 'en_core_web_sm', the following warning appears:
#UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based
#on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the 
#small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
#You can always add your own word vectors, or use one of the larger models instead if available.
#Reviewing the resukts, outisde of the first word being the same, all other levels are clearly much lower; when running 'md'
#there were several high 90% similarities, while with 'sm' no word comparison surpassed 60%

#--------------------movie comparison--------------------#

def find_most_similar_movie(movies):
    Planet_Hulk_description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
    the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately,
    Hulk lands on the planet Saakar where he is sold into slavery and trained as a gladiator"""
    Planet_Hulk_doc = nlp(Planet_Hulk_description)

    max_similarity = -1
    most_similar_movie = ""

    for title, description in movies.items():
        suggested_movie_doc = nlp(description)
        similarity_score = Planet_Hulk_doc.similarity(suggested_movie_doc)

        if similarity_score > max_similarity:
            max_similarity = similarity_score
            most_similar_movie = title
    
    return most_similar_movie

movies = {"Movie A" :"When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
"Movie B" :"After the death of Superman, several new people present themselves as possible successors.",
"Movie C" :"A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
"Movie D" :"A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
"Movie E" :"A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
"Movie F" :"In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
"Movie G" :"The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
"Movie H" :"A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
"Movie I" :"Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.",
"Movie J" :"Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."
}

most_similar = find_most_similar_movie(movies)
print("\nMost similar movie:", most_similar)