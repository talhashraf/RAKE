"""Project utilities"""
import re
import math
import unicodedata


def remove_white_spaces(input_string):
    """Removes white space characters in a string."""
    return re.sub(r'\s+', ' ', input_string).strip()

def remove_unicode_characters(input_string):
    """Removes unicode characters in the string.
    If the input string is a instance of unicode it normalizes
    the string and then returns ascii."""
    if isinstance(input_string, unicode):
        return unicodedata.normalize('NFKD', input_string)\
                          .encode('ascii', 'ignore')
    return input_string.encode('ascii', 'ignore')

def process_string(input_string):
    """Combination of remove_white_spaces() and remove_unicode_characters()."""
    return remove_white_spaces(remove_unicode_characters(input_string))

def split_words(phrase, word_size=0):
    """Return a list of words in a list"""
    words = list()
    for word in re.compile(r'[^a-zA-Z0-9_\+\-/]').split(phrase):
        if word and len(word) > word_size and not word.isdigit():
            words.append(word)
    return words

def occurrences_of_word(word, input_string):
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), input_string))

def occurrences_of_word_in_list(word, input_list):
    return sum(occurrences_of_word(word, input_string) for input_string in input_list)

def tfidf(word, words, phrase, sentences):
    tf = occurrences_of_word(word, phrase) / len(words)
    idf = math.log(len(sentences) / (1 + occurrences_of_word_in_list(word, sentences)))
    return tf * idf
