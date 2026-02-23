"""
DAY 2 — TOKENIZATION USING NLTK

WHY THIS FILE EXISTS:
- Day 1 used basic string splitting (.split())
- That approach fails for real-world text (punctuation, contractions)

WHAT WE LEARN HERE:
- Proper tokenization using NLTK
- Difference between naive and NLP-based tokenization

LEARNING OUTCOME:
- Understand how text is broken into meaningful units (tokens)
- Build foundation for preprocessing pipeline (Day 3)

NOTE:
- NLTK requires tokenizer data ('punkt')
- We ensure it's installed safely without re-downloading every time
"""

import nltk
from nltk.tokenize import word_tokenize

# ✅ Ensure 'punkt' is available (runs only if missing)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

# Step 1: Take input
text = input("Enter your mood: ")

# Step 2: Normalize text
text = text.lower()

# Step 3: Tokenize
tokens = word_tokenize(text)

# Step 4: Output
print("Tokens:", tokens)


# ------------------ LEARNING NOTES ------------------
# 1. Tokenization is NOT just splitting by space
# 2. NLP tokenizers understand punctuation and language rules
# 3. Output tokens may include punctuation (handled in Day 3)
# 4. Good preprocessing = better AI performance later