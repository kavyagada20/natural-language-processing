# Experiment 06 — Text Similarity in Natural Language Processing

## Overview

Text similarity is an important task in Natural Language Processing (NLP) that measures how similar two pieces of text are. It is widely used in applications such as search engines, recommendation systems, plagiarism detection, and document clustering.

Text similarity helps machines determine whether two sentences or documents convey the same meaning or share similar content.

In this experiment, we compute similarity between sentences using **TF-IDF vectorization and cosine similarity**.

---

## Theory

Text similarity can be calculated using different approaches, including lexical similarity, semantic similarity, and vector space models.

One of the most common techniques used in NLP is the **Vector Space Model (VSM)**.

In this model:

1. Text documents are converted into numeric vectors using techniques such as **TF-IDF (Term Frequency–Inverse Document Frequency)**.
2. Similarity between vectors is measured using **Cosine Similarity**.

### TF-IDF

TF-IDF represents how important a word is to a document relative to a collection of documents.

- **Term Frequency (TF):** Number of times a word appears in a document.
- **Inverse Document Frequency (IDF):** Importance of the word across all documents.

### Cosine Similarity

Cosine similarity measures the angle between two vectors.

Formula:
cosine_similarity(A,B) = (A · B) / (||A|| ||B||)


Values range between:

| Value | Meaning |
|------|--------|
| 1 | Identical text |
| 0 | No similarity |

---

## How to Run the Experiment

### Step 1 — Activate Conda Environment

conda activate nlp



cosine_similarity(A,B) = (A · B) / (||A|| ||B||)


Values range between:

| Value | Meaning |
|------|--------|
| 1 | Identical text |
| 0 | No similarity |

---

## How to Run the Experiment

### Step 1 — Activate Conda Environment


conda activate nlp


### Step 2 — Install Required Libraries


pip install scikit-learn matplotlib seaborn


### Step 3 — Run the Python Script


python 06_text_similarity.py


The program will:

1. Convert sentences into TF-IDF vectors
2. Compute cosine similarity
3. Display similarity matrix
4. Save a visualization image

---

## Real World Applications

### Search Engines
Search engines use text similarity to find relevant documents based on user queries.

### Plagiarism Detection
Similarity algorithms compare documents to detect copied content.

### Recommendation Systems
Used to recommend similar articles, products, or movies.

### Chatbots
Helps identify the most relevant response to user input.

### Document Clustering
Grouping similar documents together in large datasets.

---

## Conclusion

Text similarity techniques allow machines to measure how closely related pieces of text are. By representing documents as vectors and computing cosine similarity, NLP systems can efficiently compare large amounts of text and extract meaningful relationships.