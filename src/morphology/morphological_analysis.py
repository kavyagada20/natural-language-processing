"""
NLP Task: Morphological Analysis

Objective:
Perform stemming and lemmatization and visualize results.
"""

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Download Resources
# -----------------------------
nltk.download('punkt')
nltk.download('wordnet')

# -----------------------------
# Step 2: Sample Text
# -----------------------------
text = "playing played studies running better flying happiness"

print("\nOriginal Text:\n", text)

# -----------------------------
# Step 3: Tokenization
# -----------------------------
tokens = word_tokenize(text)

print("\nTokens:\n", tokens)

# -----------------------------
# Step 4: Stemming
# -----------------------------
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]

print("\nStemmed Words:\n", stemmed_words)

# -----------------------------
# Step 5: Lemmatization
# -----------------------------
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

print("\nLemmatized Words:\n", lemmatized_words)

# -----------------------------
# Step 6: Visualization
# -----------------------------
labels = ["Original", "Stemmed", "Lemmatized"]
counts = [len(tokens), len(stemmed_words), len(lemmatized_words)]

plt.figure(figsize=(6,4))
plt.bar(labels, counts)

plt.title("Morphological Analysis Comparison")
plt.xlabel("Type")
plt.ylabel("Word Count")

# Save as JPEG
plt.savefig("morphological_analysis.jpeg")

print("\nVisualization saved as morphological_analysis.jpeg")

plt.show()