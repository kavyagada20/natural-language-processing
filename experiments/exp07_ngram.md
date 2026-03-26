# Experiment 07 — N-Gram Language Model in Natural Language Processing

## Overview

An N-Gram language model is a statistical language model used in Natural Language Processing to predict the probability of a sequence of words. It works by analyzing contiguous sequences of *n* words from a text corpus.

N-grams are commonly used in text generation, speech recognition, autocomplete systems, and machine translation.

In this experiment, we generate **bigrams and trigrams** from a sample text and visualize the frequency distribution of the most common N-grams.

---

## Theory

An **N-gram** is a sequence of *n* consecutive words from a given text.

Examples:

| Type | Example |
|-----|--------|
| Unigram (1-gram) | natural |
| Bigram (2-gram) | natural language |
| Trigram (3-gram) | natural language processing |

The probability of a word sequence in an N-gram model is calculated using conditional probability.

For example:
conda activate nlp


### Step 2 — Install Required Libraries


pip install nltk matplotlib seaborn


### Step 3 — Run the Python Script


python 07_ngram_language_model.py


The program will:

1. Tokenize the text
2. Generate bigrams and trigrams
3. Compute frequency counts
4. Save results to files
5. Create a visualization of N-gram frequencies

---

## Real World Applications

### Autocomplete Systems
Search engines and messaging apps use N-grams to predict the next word.

### Speech Recognition
Helps determine the most probable word sequences in spoken language.

### Machine Translation
N-grams help model linguistic patterns in translation systems.

### Text Generation
Used in predictive text generation and language modeling.

### Spell Checking
N-gram models help detect unusual word sequences.

---

## Conclusion

N-gram language models provide a simple yet effective statistical approach to modeling language patterns. By analyzing sequences of words, they help NLP systems understand contextual relationships between words and predict future tokens in a sequence.