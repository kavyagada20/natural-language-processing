"""
Experiment 09: NLP Application - Sentiment Analysis

Objective:
To demonstrate a practical NLP application by performing
sentiment analysis on sample sentences.

The program will:
1. Analyze sentiment polarity
2. Classify sentences as Positive, Negative, or Neutral
3. Save results to a text file
4. Generate a sentiment distribution chart
"""

# Import required libraries
from textblob import TextBlob
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Sample Input Sentences
# -----------------------------
sentences = [
    "Natural language processing is an exciting field.",
    "I love working on machine learning projects.",
    "This assignment is very difficult.",
    "The results of the experiment are disappointing.",
    "The system works perfectly and efficiently."
]

# Store sentiment results
results = []

print("\nSentiment Analysis Results\n")

# -----------------------------
# Step 2: Perform Sentiment Analysis
# -----------------------------
for sentence in sentences:

    # Create TextBlob object
    blob = TextBlob(sentence)

    # Get sentiment polarity
    polarity = blob.sentiment.polarity

    # Classify sentiment
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Save result
    results.append(sentiment)

    # Print result
    print(f"Sentence : {sentence}")
    print(f"Polarity : {polarity:.2f}")
    print(f"Sentiment: {sentiment}\n")


# -----------------------------
# Step 3: Sentiment Distribution
# -----------------------------
labels = ["Positive", "Negative", "Neutral"]

values = [
    results.count("Positive"),
    results.count("Negative"),
    results.count("Neutral")
]


# -----------------------------
# Step 4: Plot Sentiment Chart
# -----------------------------
plt.figure(figsize=(6,4))

plt.bar(labels, values)

plt.title("Sentiment Analysis Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

# Save chart
plt.savefig("sentiment_analysis_chart.png")

print("Sentiment chart saved as sentiment_analysis_chart.png")


# -----------------------------
# Step 5: Save Results to File
# -----------------------------
with open("sentiment_results.txt", "w") as file:

    for sentence, sentiment in zip(sentences, results):
        file.write(f"{sentence} -> {sentiment}\n")

print("Sentiment results saved to sentiment_results.txt")

# Show chart
plt.show()