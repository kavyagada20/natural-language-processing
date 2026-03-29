"""
NLP Application: Sentiment Analysis

Objective:
Analyze sentiment of text using TextBlob
and visualize the results.
"""

from textblob import TextBlob
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Sample Input Data
# -----------------------------
sentences = [
    "I love natural language processing.",
    "This project is very interesting and useful.",
    "The results are not good.",
    "I am disappointed with the performance.",
    "The system works perfectly."
]

# -----------------------------
# Step 2: Sentiment Analysis
# -----------------------------
results = []

print("\nSentiment Analysis Results:\n")

for sentence in sentences:
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    results.append(sentiment)

    print(f"{sentence} -> {sentiment} ({polarity:.2f})")

# -----------------------------
# Step 3: Count Sentiments
# -----------------------------
labels = ["Positive", "Negative", "Neutral"]
values = [
    results.count("Positive"),
    results.count("Negative"),
    results.count("Neutral")
]

# -----------------------------
# Step 4: Visualization
# -----------------------------
plt.figure(figsize=(6,4))
plt.bar(labels, values)

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

# Save as JPEG (as requested)
plt.savefig("sentiment_analysis.jpeg")

print("\nChart saved as sentiment_analysis.jpeg")

plt.show()