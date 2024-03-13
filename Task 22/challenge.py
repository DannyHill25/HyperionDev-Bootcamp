# Practical Interview test based on the 'Little Sister's Vocabulary'

# Challenge 1: Add a prefix to a word

def add_prefix_un(word):
    """
    Add prefix 'un-' to input word

    Parameters
    ---------------
    word:  str

    Returns
    ----------
    word given with prefix 'un-'
    """
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    return "un" + word


# Challenge 2: Add a prefix to a group of words

def make_word_groups(vocab_words):
    """
    Add given prefix to a group of words

    Parameters
    ---------------
    vocab_words: list
        Lit of wordsd with first entry being the prefix and the rest the words given

    Returns
    ----------
    str of a list starting with the prefix, followed by the words with the prefix
    """
    if not isinstance(vocab_words, list):
        raise TypeError("Input must be a list")
    if len(vocab_words) < 2:
        raise ValueError("Input list must contain at least one prefix and one word")
    
    # Isolate the prefix
    prefix = vocab_words[0]
    # Group the words in a list
    words = vocab_words[1:]

    # Iterate through the list to add the prefix
    words_group = [prefix] + [prefix + word for word in words]

    return " :: ".join(words_group)


# Challenge 3: Remove a suffix from a word

def remove_suffix_ness(word):
    """
    Remove suffix '-ness' from given word

    Parameters
    ---------------
    word: str
        word ending in '-ness'

    Returns
    ----------
    root word
    """
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    if not word.endswith("ness"):
        raise ValueError("Input word must end with '-ness'")
    
    # Remove suffix
    removed_suffix = word[:-4]

    # Change 'i' for 'y'
    if removed_suffix.endswith("i"):
        removed_suffix = removed_suffix.replace('i','y', 1)

    return removed_suffix


# Challenge 4: Extract an adjective and convert it into a verb

def adjective_to_verb(sentence, index):
    """
    Convert adjective in a sentence to a verb by adding '-en'

    Parameters
    ---------------
    sentence: str
    
    index: int
        position of the adjective in the sentence

    Returns
    ----------
    adjective of the sentence as a verb
    """
    if not isinstance(sentence, str):
        raise TypeError("Please enter a sentence as a string")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    
    # Ensure that index is within the range of the sentence
    words = sentence.split()
    if index < 0 or index >= len(words):
        raise ValueError("Index is out of range")

    # Isolate adjective from the sentence
    adjective = words[index]
    
    # Add 'en' to adjective, accounting for cases were adjective ends in 'y'
    if adjective.endswith('y'):
        verb = adjective[:-1] + 'ie' + "en"
    else:
        verb = adjective + "en"

    return verb


prefixed_word = add_prefix_un("satisfied")
print(prefixed_word)

word_group = make_word_groups(['auto', 'didactic', 'graph', 'mate'])
print(word_group)

root_word = remove_suffix_ness("happiness")
print(root_word)

sentence_verd = adjective_to_verb('It got dark as the sun set.', 2)
print(sentence_verd)