#my thought process here is turn the document into a list and then somehow scan the list for duplicates

import string
from collections import Counter

inputFile = input('Enter your text file name here: ')
outputFile = 'counted.txt'

def text_cleaner(text):
    text = text.lower()  # makes entire file lowercase
    text = text.translate(str.maketrans('','', string.punctuation)) # This creates a translation table where all punctuation characters (defined in string.punctuation) are mapped to None, effectively removing them from the text.
    return text

def wordFrequencyCounter(inputFile, outputFile):
    #opens file and saves a editable copy in the cache
    with open(inputFile,'r') as file:
        text = file.read()

    #cleans text and splits into words
    cleaned_text = text_cleaner(text)
    words = cleaned_text.split()  # seperates string anywhere there is whitespace.

    word_counts = Counter(words) #Counter takes an iterable as input and counts how many times each element appears. imported from the collections python module
    print(word_counts)

    with open(outputFile, 'w') as file:          # this with statement jus ensures that any files are properly closed
        for word, count in word_counts.items():  # Loops through each key-value pair in the word_counts dictionary, word is a string (the word itself), and count is an integer (its frequency).
            file.write(f"{word}: {count}\n")     # Writes each word and its count to the file in the format: <word>: <count> followed by a newline (\n). f just means a variable can be inserted.
    
    print(f"Word frequencies saved to {outputFile}")

    
    
