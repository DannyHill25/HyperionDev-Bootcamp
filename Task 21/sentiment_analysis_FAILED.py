import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from os import chdir, path      

# Load spaCy model
nlp = spacy.load("en_core_web_md")

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

# Function for cleaning the text
def cleaning_text(text):
    """
    Clean the data for tokenization

    Parameters
    ---------------
    text: list of entries

    Returns
    ----------
    List of entries in lower case, without punctuation, special characters or whitespaces
    """
    # Check if text is a string and not empty
    if isinstance(text, str) and text.strip():
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
    text: list of entries

    Returns
    ----------
    List of tokens from each entry
    """
    # Check if text is a string and not empty
    if isinstance(text, str) and text.strip():
        # Tokenize text using spaCy
        tokens = nlp(text)
        # Filter out stop words and punctuation
        tokens = [token.text for token in tokens if not token.is_stop and token.is_alpha]
        return tokens
    else:
        return []  # Return empty list for non-text or empty values  

# Function for sentiment analysis
def analyse_sentiment(text):
    """
    Analyse the sentiment of each entry

    Parameters
    ---------------
    text: list of entries

    Returns
    ----------
    An assigned sentiment of 'Positive', 'Negative' or 'Neutral'
    """
    try:
        doc = nlp(text)
        # Get sentiment score using spaCy's textblob
        sentiment_score = doc.polarity
        if sentiment_score > 0:
            return 'Positive'
        elif sentiment_score < 0:
            return 'Negative'
        else:
            return 'Neutral'
    except AttributeError:
        return 'Neutral'

# Apply text cleaning
full_reviews_text_column['clean_text'] = full_reviews_text_column['reviews.text'].apply(cleaning_text)

# Apply text tokenization
full_reviews_text_column['token_text'] = full_reviews_text_column['clean_text'].apply(tokenize_text)

# Apply sentiment analysis
full_reviews_text_column['sentiment'] = full_reviews_text_column['token_text'].apply(analyse_sentiment)

# Display the results
print(full_reviews_text_column[['reviews.text', 'sentiment']])

# Display the count of neutral, positive, and negative reviews
sentiment_counts = full_reviews_text_column['sentiment'].value_counts()
print("Count of reviews by sentiment:")
print(sentiment_counts)