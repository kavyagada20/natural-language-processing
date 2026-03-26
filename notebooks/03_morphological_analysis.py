"""
Experiment 03: Morphological Analysis

Objective:
To demonstrate morphological analysis using stemming
techniques provided by the NLTK library.
"""

# Import required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required tokenizer
nltk.download('punkt')

# Sample input sentence
text = "playing played plays running runner studies studying happiness"

# Tokenize the sentence into individual words
tokens = word_tokenize(text)

# Initialize Porter Stemmer
stemmer = PorterStemmer()

print("\nMorphological Analysis using Stemming:\n")

# Perform stemming for each word
for word in tokens:
    root_word = stemmer.stem(word)
    print(f"{word} -> {root_word}")