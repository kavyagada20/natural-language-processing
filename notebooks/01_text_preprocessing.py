"""
Experiment 01: Text Preprocessing in Natural Language Processing

Objective:
Demonstrate common NLP preprocessing steps:
1. Lowercasing
2. Removing punctuation
3. Tokenization
4. Stopword removal
5. Stemming
"""

# ------------------------------
# Import Required Libraries
# ------------------------------

import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# ------------------------------
# Download Required NLTK Data
# (Fix added for punkt_tab)
# ------------------------------

nltk.download('punkt')
nltk.download('punkt_tab')   # NEW: required for latest nltk versions
nltk.download('stopwords')


# ------------------------------
# Step 1: Input Text
# ------------------------------

text = "Natural Language Processing is amazing! It helps computers understand human language."

print("\nOriginal Text:")
print(text)


# ------------------------------
# Step 2: Convert Text to Lowercase
# ------------------------------

text_lower = text.lower()

print("\nLowercase Text:")
print(text_lower)


# ------------------------------
# Step 3: Remove Punctuation
# ------------------------------

clean_text = re.sub(r'[^a-zA-Z\s]', '', text_lower)

print("\nCleaned Text (No punctuation):")
print(clean_text)


# ------------------------------
# Step 4: Tokenization
# ------------------------------

tokens = word_tokenize(clean_text)

print("\nTokens:")
print(tokens)


# ------------------------------
# Step 5: Stopword Removal
# ------------------------------

stop_words = set(stopwords.words('english'))

filtered_words = [word for word in tokens if word not in stop_words]

print("\nAfter Stopword Removal:")
print(filtered_words)


# ------------------------------
# Step 6: Stemming
# ------------------------------

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("\nStemmed Words:")
print(stemmed_words)


# ------------------------------
# Final Output
# ------------------------------

print("\nFinal Preprocessed Output:")
print(stemmed_words)