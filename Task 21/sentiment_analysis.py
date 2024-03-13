import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from os import chdir, path      

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Enable TextBlob extension
nlp.add_pipe('spacytextblob')

# Get the name of the current running Python file
this_file = path.dirname(__file__)

# Make all paths read by this file resolve from this directory
chdir(this_file)

# Load 'reviews.text' column from CSV file
original_reviews_text_column = pd.read_csv("amazon_product_reviews.csv", usecols=['reviews.text'], dtype={'reviews.text': 'str'})

# Remove any empty entries
full_reviews_text_column = original_reviews_text_column.dropna()

# Select sample
sample_reviews = full_reviews_text_column.sample(2)['reviews.text'].tolist()

# Function for cleaning the text
def cleaning_text(text):
    """
    Clean the data for tokenization

    Parameters
    ---------------
    text: list or str
        List of entries or a single entry

    Returns
    ----------
    List of entries in lower case, without punctuation, special characters or whitespaces
    """
    if isinstance(text, list):
        cleaned_texts = []
        for entry in text:
            cleaned_entry = cleaning_text(entry)  # Recursively clean each entry
            cleaned_texts.append(cleaned_entry)
        return cleaned_texts
    elif isinstance(text, str) and text.strip():
        # Convert text to lowercase
        text = text.lower()
        # Remove punctuation and special characters
        text = ''.join([char for char in text if char.isalnum() or char.isspace()])
        # Remove extra whitespaces
        text = ' '.join(text.split())
        return text
    else:
        return ''  # Return empty string for non-text or empty values


# Function for tokenization
def tokenize_text(text):
    """
    Tokenize data for sentiment analysis

    Parameters
    ---------------
    text: list
        List of entries to be tokenized

    Returns
    ----------
    List of lists of tokens from each entry
    """
    tokenized_texts = []
    for entry in text:
        if isinstance(entry, str) and entry.strip():
            # Tokenize text using spaCy
            tokens = nlp(entry)
            # Filter out stop words and punctuation
            tokens = [token.text for token in tokens if not token.is_stop and token.is_alpha]
            tokenized_texts.append(tokens)
        else:
            tokenized_texts.append([])  # Append empty list for non-text or empty values
    return tokenized_texts


# Function for sentiment analysis
def analyse_sentiment(tokenized_reviews):
    """
    Analyse the sentiment of each entry

    Parameters
    ---------------
    tokenized_reviews: list of lists of tokens
        List of tokenized reviews

    Returns
    ----------
    List of assigned sentiments for each review ('Positive', 'Negative', or 'Neutral')
    """
    sentiments = []
    for tokens in tokenized_reviews:
        # Join tokens into a single string for sentiment analysis
        text = ' '.join(tokens)
        doc = nlp(text)
        # Get sentiment score using spaCy's textblob
        sentiment_score = doc._.polarity
        if sentiment_score > 0:
            sentiments.append('Positive')
        elif sentiment_score < 0:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')
    return sentiments


# Function to determine similiraty
def analyse_similarity(tokenized_review1, tokenized_review2):
    """
    Calculate the similarity between two tokenized reviews

    Parameters
    ---------------
    tokenized_review1: list
        List of tokens for the first review
    tokenized_review2: list
        List of tokens for the second review

    Returns
    ----------
    Similarity score between the two reviews (float)
    """
    # Join tokens into a single string for similarity calculation
    text1 = ' '.join(tokenized_review1)
    text2 = ' '.join(tokenized_review2)
    
    # Create spaCy Doc objects for the tokenized reviews
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    
    # Calculate similarity between the two Doc objects
    review_similarity = doc1.similarity(doc2)

    # Round the similarity score to three decimal places and convert into a percentage
    review_similarity = round(review_similarity*100, 2)
    
    return review_similarity


# Apply text cleaning
cleaned_sample_reviews = cleaning_text(sample_reviews)

# Apply text tokenization
tokenized_sample_reviews = tokenize_text(cleaned_sample_reviews)

# Apply sentiment analysis
sentiments = analyse_sentiment(tokenized_sample_reviews)

# Apply similarity analysis
similarity_score = analyse_similarity(tokenized_sample_reviews[0], tokenized_sample_reviews[1])

# Display the results
for i in range(2):
    print("\nReview:", sample_reviews[i])
    print("Sentiment:", sentiments[i])
print("\nSimilarity score:", similarity_score,"%")
