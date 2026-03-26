# Experiment 04 — Chunking in Natural Language Processing

## Overview

Chunking, also known as shallow parsing, is a Natural Language Processing technique used to group words into meaningful units or phrases based on their grammatical structure. These groups are commonly referred to as chunks.

Chunking helps identify syntactic structures such as noun phrases, verb phrases, and prepositional phrases without performing full syntactic parsing.

In this experiment, we demonstrate chunking using the **Natural Language Toolkit (NLTK)** library by identifying noun phrases from a sentence.

---

## Theory

Chunking is the process of grouping tokens into syntactically correlated parts of a sentence. It operates on the output of **Part-of-Speech (POS) tagging**, which labels each word according to its grammatical category.

The primary goal of chunking is to identify meaningful phrase structures in a sentence.

Common types of chunks include:

| Chunk Type | Description | Example |
|-----------|-------------|--------|
| Noun Phrase (NP) | Group of words centered around a noun | the red car |
| Verb Phrase (VP) | Phrase containing the main verb | is running |
| Prepositional Phrase (PP) | Phrase beginning with a preposition | in the room |

Example sentence:

"The quick brown fox jumps over the lazy dog."

Noun Phrase chunks:

- The quick brown fox  
- the lazy dog

Chunking typically follows these steps:

1. Tokenization  
2. Part-of-Speech Tagging  
3. Chunk Pattern Definition  
4. Chunk Extraction

In this experiment, **NLTK’s RegexpParser** is used to define grammar rules for extracting noun phrases.

---

## How to Run the Experiment

### Step 1 — Activate Conda Environment

### Step 2 — Install Required Library


pip install nltk


### Step 3 — Run the Python Script


python 04_chunking.py


The program will tokenize the sentence, perform POS tagging, and extract noun phrase chunks.

---

## Real World Applications

### Information Extraction
Chunking helps identify meaningful phrases from text, which can be used to extract useful information.

### Question Answering Systems
Helps identify key entities and phrases relevant to answering user queries.

### Chatbots and Conversational AI
Chunking allows chatbots to understand sentence structure and user intent more accurately.

### Text Summarization
Helps identify important phrases that should be included in summaries.

### Search Engines
Chunking improves query understanding and document indexing.

---

## Conclusion

Chunking is a fundamental technique in Natural Language Processing that helps identify meaningful phrases in a sentence. By grouping words based on grammatical patterns, chunking improves the performance of many NLP tasks such as information extraction, question answering, and text summarization.