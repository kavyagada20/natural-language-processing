# Experiment 02 — Named Entity Recognition (NER)

## Overview

Named Entity Recognition (NER) is an important task in Natural Language Processing (NLP) that focuses on identifying and classifying named entities present in textual data. Named entities typically include names of people, organizations, locations, dates, monetary values, and other specific categories.

NER helps convert unstructured text into structured information that machines can easily understand and analyze.

In this experiment, we use the **spaCy NLP library** to detect named entities from a given input text.

---

# Theory

Named Entity Recognition is a subtask of information extraction in NLP. It involves locating and categorizing entities within text into predefined categories.

Typical entity categories include:

| Entity Type | Description | Example |
|-------------|-------------|---------|
| PERSON | Names of people | Elon Musk |
| ORG | Organizations | Google |
| GPE | Countries or cities | India |
| DATE | Dates | January 2024 |
| MONEY | Monetary values | $100 |

NER systems use machine learning or deep learning models trained on large datasets to understand linguistic patterns and contextual relationships between words.

Modern NLP frameworks such as **spaCy** provide pretrained models that allow developers to perform NER without training models from scratch.

The typical workflow for NER includes:

1. Text preprocessing  
2. Tokenization  
3. Contextual analysis  
4. Entity classification

---


The script will process the input text and print the detected named entities along with their labels.

---

# Real World Applications

Named Entity Recognition has several practical applications in modern NLP systems.

### Information Extraction
NER helps extract structured information such as names of people, companies, and locations from large text datasets.

### Search Engines
Search engines use NER to better understand user queries and improve search result relevance.

### Chatbots and Virtual Assistants
NER helps conversational AI systems identify references to entities such as people, locations, and organizations.

### Financial Analysis
NER can identify company names, stock information, and financial terms from news articles and financial reports.

### Healthcare Text Analysis
NER is used to detect medical entities such as diseases, medications, and treatments in clinical documents.

---

# Conclusion

Named Entity Recognition plays a critical role in transforming unstructured textual information into structured knowledge. By identifying important entities within text, NER enables intelligent information extraction and enhances the capabilities of many NLP applications.
