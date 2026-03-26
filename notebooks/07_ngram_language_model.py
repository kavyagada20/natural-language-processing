"""
Experiment 07: N-Gram Language Model
Generate bigrams and trigrams and visualize their frequencies.
"""

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Download tokenizer
nltk.download('punkt')

# -----------------------------
# Step 1: Sample Text
# -----------------------------
text = """
Natural language processing enables computers to understand human language.
Language models help predict sequences of words in natural language.
"""

# -----------------------------
# Step 2: Tokenization
# -----------------------------
tokens = word_tokenize(text.lower())

# -----------------------------
# Step 3: Generate N-Grams
# -----------------------------
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

# -----------------------------
# Step 4: Frequency Counts
# -----------------------------
bigram_freq = Counter(bigrams)
trigram_freq = Counter(trigrams)

print("\nTop 10 Bigrams:\n")
for bg, freq in bigram_freq.most_common(10):
    print(bg, "->", freq)

print("\nTop 10 Trigrams:\n")
for tg, freq in trigram_freq.most_common(10):
    print(tg, "->", freq)

# -----------------------------
# Step 5: Save Results to File
# -----------------------------
with open("ngram_results.txt", "w") as f:
    f.write("Top Bigrams\n")
    for bg, freq in bigram_freq.most_common(10):
        f.write(f"{bg} -> {freq}\n")

    f.write("\nTop Trigrams\n")
    for tg, freq in trigram_freq.most_common(10):
        f.write(f"{tg} -> {freq}\n")

print("\nResults saved to ngram_results.txt")

# -----------------------------
# Step 6: Visualization
# -----------------------------
top_bigrams = bigram_freq.most_common(5)

labels = [" ".join(bg) for bg, _ in top_bigrams]
values = [freq for _, freq in top_bigrams]

plt.figure(figsize=(6,4))
sns.barplot(x=values, y=labels)

plt.title("Top Bigrams Frequency")
plt.xlabel("Frequency")
plt.ylabel("Bigram")

plt.tight_layout()

# Save visualization
plt.savefig("ngram_frequency.png")

print("\nVisualization saved as ngram_frequency.png")

plt.show()