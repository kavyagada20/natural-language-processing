"""
NLP Application: Plagiarism Detection

Objective:
Detect similarity between documents using TF-IDF and cosine similarity.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Step 1: Sample Documents
# -----------------------------
documents = [
    "Natural language processing is a field of artificial intelligence.",
    "NLP is a branch of AI that helps computers understand human language.",
    "Machine learning models are widely used in artificial intelligence.",
    "Natural language processing enables machines to understand human language."
]

# -----------------------------
# Step 2: TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# -----------------------------
# Step 3: Compute Similarity
# -----------------------------
similarity_matrix = cosine_similarity(tfidf_matrix)

print("\nPlagiarism Detection (Similarity Matrix):\n")
print(similarity_matrix)

# -----------------------------
# Step 4: Identify High Similarity
# -----------------------------
threshold = 0.5

print("\nPotential Plagiarism Cases:\n")

for i in range(len(documents)):
    for j in range(i + 1, len(documents)):
        if similarity_matrix[i][j] > threshold:
            print(f"Document {i+1} and Document {j+1} -> Similarity: {similarity_matrix[i][j]:.2f}")

# -----------------------------
# Step 5: Save Results
# -----------------------------
np.savetxt("plagiarism_results.txt", similarity_matrix)

# -----------------------------
# Step 6: Visualization
# -----------------------------
plt.figure(figsize=(6,5))

plt.imshow(similarity_matrix, interpolation='nearest')
plt.colorbar()

plt.title("Plagiarism Detection Heatmap")
plt.xlabel("Document")
plt.ylabel("Document")

# Save as JPEG
plt.savefig("plagiarism_heatmap.jpeg")

print("\nHeatmap saved as plagiarism_heatmap.jpeg")

plt.show()