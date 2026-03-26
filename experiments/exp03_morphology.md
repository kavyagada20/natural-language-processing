# Experiment 03 — Morphological Analysis

## Overview

Morphological Analysis is an important concept in Natural Language Processing (NLP) that focuses on analyzing the internal structure of words. It helps identify the root forms of words and understand how words are constructed using prefixes, suffixes, and stems.

Morphological analysis allows NLP systems to reduce different word variations into their base forms, improving the efficiency of text processing and language understanding.

This experiment demonstrates morphological analysis using **stemming techniques provided by the NLTK library**.

---

## Theory

Morphology is the branch of linguistics that studies the structure and formation of words. Words can be decomposed into smaller meaningful units known as **morphemes**.

A morpheme is the smallest unit of meaning in a language.

There are two main types of morphemes:

| Type | Description | Example |
|-----|-------------|--------|
| Root | Base form of a word | play |
| Affix | Prefix or suffix added to root | replay, playing |

Examples of morphological transformations:

| Word | Root Form |
|-----|-----------|
| playing | play |
| running | run |
| studies | study |
| happiness | happy |

Morphological analysis helps NLP systems recognize these relationships and treat related words as variations of the same concept.

In this experiment, **Porter Stemmer** from the NLTK library is used to perform stemming, which reduces words to their base or root form.

---

## How to Run the Experiment

### Step 1 — Activate Conda Environment

### Step 2 — Install Required Library


pip install nltk


### Step 3 — Run the Python Script


python 03_morphological_analysis.py


The program will analyze the words and display their root forms.

---

## Real World Applications

### Search Engines
Morphological analysis helps search engines understand variations of words. For example, searching for "run" can also retrieve results containing "running" or "runs".

### Machine Translation
It improves translation accuracy by identifying the base form of words before translating them into another language.

### Text Classification
Helps reduce vocabulary size by grouping multiple word variations under a single root word.

### Information Retrieval
Improves document matching by identifying similar word forms.

### Speech Recognition Systems
Helps systems recognize variations of spoken words and map them to their base forms.

---

## Conclusion

Morphological analysis plays a crucial role in understanding the structure of words in natural langu