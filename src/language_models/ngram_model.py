"""
NLP Language Model: N-Gram Model

Objective:
Generate bigrams and trigrams, analyze frequency,
and visualize most frequent n-grams.
"""

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Download Resources
# -----------------------------
nltk.download('punkt')
nltk.download('punkt_tab')

# -----------------------------
# Step 2: Sample Text
# -----------------------------
text = """
Natural language processing enables machines to understand human language.
Language models are essential in natural language processing tasks.
"""

print("\nOriginal Text:\n", text)

# -----------------------------
# Step 3: Tokenization
# -----------------------------
tokens = word_tokenize(text.lower())

print("\nTokens:\n", tokens)

# -----------------------------
# Step 4: Generate N-Grams
# -----------------------------
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

# -----------------------------
# Step 5: Frequency Analysis
# -----------------------------
bigram_freq = Counter(bigrams)
trigram_freq = Counter(trigrams)

print("\nTop Bigrams:\n")
for bg, freq in bigram_freq.most_common(5):
    print(bg, "->", freq)

print("\nTop Trigrams:\n")
for tg, freq in trigram_freq.most_common(5):
    print(tg, "->", freq)

# -----------------------------
# Step 6: Visualization
# -----------------------------
top_bigrams = bigram_freq.most_common(5)

labels = [" ".join(bg) for bg, _ in top_bigrams]
values = [freq for _, freq in top_bigrams]

plt.figure(figsize=(6,4))
plt.barh(labels, values)

plt.title("Top Bigrams Frequency")
plt.xlabel("Frequency")
plt.ylabel("Bigrams")

plt.tight_layout()

# Save as JPEG
plt.savefig("ngram_model_output.jpeg")

print("\nVisualization saved as ngram_model_output.jpeg")

plt.show()