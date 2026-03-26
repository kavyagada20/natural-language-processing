"""
Experiment 02: Named Entity Recognition (NER)

Objective:
To identify named entities in text using the spaCy NLP library.
"""

# Import spaCy library
import spacy

# Load the pretrained English NLP model
# This model contains linguistic rules and entity recognition capabilities
nlp = spacy.load("en_core_web_sm")

# Sample input text
text = "Elon Musk founded SpaceX and Tesla. He was born in South Africa and now lives in the United States."

# Process the text using spaCy
doc = nlp(text)

# Print detected entities
print("\nNamed Entities Detected:\n")

# Loop through detected entities
for entity in doc.ents:
    print(f"Entity: {entity.text} | Label: {entity.label_}")