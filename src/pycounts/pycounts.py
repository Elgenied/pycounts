
"""This is just example on how to use Python functions """
from collections import Counter
from string import punctuation

def load_text (input_file):
    """_Load text from Text file and returns it as strings_

    Args:
        input_file (text): _Text File input _

    Returns:
        _String_: _String structure of the file _
    """
    with open(input_file, "r") as file:
        text = file.read()
        return text


def clean_text(text):
    """_”””Lowercase and remove punctuation from a string._

    Args:
        text (_string_): _String loaded from Text file _

    Returns:
        _string _: _description_
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
        return text


def count_words(input_file):
    """_Count unique words in a string_

    Args:
        input_file (_text): _description_

    Returns:
        _List_: _description_
    """
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)

print(count_words("zen.txt"))
