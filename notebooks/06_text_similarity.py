"""
Experiment 06: Text Similarity using TF-IDF and Cosine Similarity
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -----------------------------
# Step 1: Sample Sentences
# -----------------------------
documents = [
    "Natural language processing is a fascinating field",
    "Machine learning and natural language processing are closely related",
    "Deep learning improves NLP performance",
    "The cat is sleeping on the sofa"
]

# -----------------------------
# Step 2: TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

# -----------------------------
# Step 3: Cosine Similarity
# -----------------------------
similarity_matrix = cosine_similarity(tfidf_matrix)

print("\nText Similarity Matrix:\n")
print(similarity_matrix)

# -----------------------------
# Step 4: Save Output File
# -----------------------------
np.savetxt("similarity_matrix.txt", similarity_matrix)

print("\nSimilarity matrix saved to similarity_matrix.txt")

# -----------------------------
# Step 5: Visualization
# -----------------------------
plt.figure(figsize=(6,5))

sns.heatmap(similarity_matrix,
            annot=True,
            cmap="Blues",
            xticklabels=[1,2,3,4],
            yticklabels=[1,2,3,4])

plt.title("Text Similarity Matrix")
plt.xlabel("Document")
plt.ylabel("Document")

# Save figure
plt.savefig("similarity_matrix.png")

print("\nSimilarity heatmap saved as similarity_matrix.png")

plt.show()