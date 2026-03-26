"""
Experiment 05: POS Tagging using Hidden Markov Model (HMM)

Objective:
Train a Hidden Markov Model based POS tagger
and apply it to a sample sentence.
"""

import nltk
from nltk.corpus import treebank
from nltk.tag import hmm

# Download required datasets
nltk.download("treebank")
nltk.download("punkt")

# -----------------------------
# Step 1: Load training data
# -----------------------------
train_data = treebank.tagged_sents()

# -----------------------------
# Step 2: Train HMM Tagger
# -----------------------------
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train(train_data)

# -----------------------------
# Step 3: Input sentence
# -----------------------------
sentence = "Natural language processing is very interesting"

tokens = sentence.split()

# -----------------------------
# Step 4: POS Tagging
# -----------------------------
tagged_output = tagger.tag(tokens)

print("\nSentence:")
print(sentence)

print("\nPOS Tagged Output:\n")
for word, tag in tagged_output:
    print(f"{word} -> {tag}")

# -----------------------------
# Step 5: Save result to file
# -----------------------------
with open("pos_hmm_output.txt", "w") as f:
    for word, tag in tagged_output:
        f.write(f"{word} -> {tag}\n")

print("\nResult saved to pos_hmm_output.txt")