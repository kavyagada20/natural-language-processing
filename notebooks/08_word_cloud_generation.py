"""
Experiment 08: Word Cloud Generation

Objective:
Generate a word cloud visualization from a sample text
using the WordCloud Python library.
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# -----------------------------
# Step 1: Sample Text
# -----------------------------
text = """
Natural language processing enables computers to understand human language.
NLP techniques are widely used in machine learning, artificial intelligence,
chatbots, search engines, and recommendation systems.
"""

# -----------------------------
# Step 2: Remove Stopwords
# -----------------------------
stop_words = set(stopwords.words('english'))

tokens = word_tokenize(text.lower())

filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words]

clean_text = " ".join(filtered_words)

# -----------------------------
# Step 3: Generate Word Cloud
# -----------------------------
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(clean_text)

# -----------------------------
# Step 4: Display Word Cloud
# -----------------------------
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud Visualization")

# -----------------------------
# Step 5: Save Image
# -----------------------------
plt.savefig("wordcloud_output.png")

print("\nWord cloud image saved as wordcloud_output.png")

plt.show()