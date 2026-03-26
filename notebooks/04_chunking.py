"""
Experiment 04: Chunking in Natural Language Processing

Objective:
To demonstrate chunking (shallow parsing) using NLTK.
The program identifies noun phrases in a sentence using
Part-of-Speech tagging and grammar rules.
"""

# Import required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import RegexpParser


# -----------------------------
# Download Required NLTK Data
# -----------------------------
# These downloads ensure the program runs without errors

nltk.download('punkt')
nltk.download('punkt_tab')  # required for latest NLTK
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')


# -----------------------------
# Step 1: Input Sentence
# -----------------------------

sentence = "The quick brown fox jumps over the lazy dog"

print("\nInput Sentence:\n", sentence)


# -----------------------------
# Step 2: Tokenization
# -----------------------------

tokens = word_tokenize(sentence)

print("\nTokens:\n", tokens)


# -----------------------------
# Step 3: POS Tagging
# -----------------------------

tagged_words = pos_tag(tokens)

print("\nPOS Tagged Words:\n", tagged_words)


# -----------------------------
# Step 4: Define Chunk Grammar
# -----------------------------
# NP = Noun Phrase

grammar = "NP: {<DT>?<JJ>*<NN>}"

chunk_parser = RegexpParser(grammar)


# -----------------------------
# Step 5: Perform Chunking
# -----------------------------

chunk_tree = chunk_parser.parse(tagged_words)

print("\nChunk Tree:\n")
print(chunk_tree)


# -----------------------------
# Step 6: Visual Representation
# -----------------------------
# This opens a graphical tree window

chunk_tree.draw()