"""
NLP Application: Spell Checker

Objective:
Detect and correct spelling errors using TextBlob
and visualize correction statistics.
"""

from textblob import TextBlob
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Input Text
# -----------------------------
text = "Natrual langauge procesing is amazng and very powrful."

print("\nOriginal Text:\n", text)

# -----------------------------
# Step 2: Spell Correction
# -----------------------------
blob = TextBlob(text)

corrected_text = str(blob.correct())

print("\nCorrected Text:\n", corrected_text)

# -----------------------------
# Step 3: Compare Words
# -----------------------------
original_words = text.split()
corrected_words = corrected_text.split()

corrected_count = 0

print("\nCorrections:\n")

for o, c in zip(original_words, corrected_words):
    if o != c:
        corrected_count += 1
        print(f"{o} -> {c}")

unchanged_count = len(original_words) - corrected_count

# -----------------------------
# Step 4: Visualization
# -----------------------------
labels = ["Corrected Words", "Unchanged Words"]
values = [corrected_count, unchanged_count]

plt.figure(figsize=(6,4))
plt.bar(labels, values)

plt.title("Spell Checker Analysis")
plt.xlabel("Category")
plt.ylabel("Count")

# Save as JPEG
plt.savefig("spell_checker_result.jpeg")

print("\nResult saved as spell_checker_result.jpeg")

plt.show()