# ✍️ Writer Bot — Markov Chain Text Generator with Custom Hash Table

`writer_bot_ht.py` is a Python program that generates random text using a Markov chain model with customizable prefix size. Unlike typical implementations that use Python dictionaries and tuples, this version uses a custom-built **hash table** ADT with **string-based prefixes** and **linear probing** collision resolution.

---

## 📌 Program Overview

This program:
1. Reads a source text file.
2. Builds a prefix-to-suffix mapping using a custom hash table.
3. Generates a specified number of random words using the Markov chain approach.
4. Outputs the result as a space-separated string of words.

The prefix size (`n`) is configurable, and prefixes are represented as **strings** (e.g., `'Half a'`) instead of tuples. This implementation ensures deterministic behavior by using a fixed random seed.

---

## ⚙️ How It Works

1. **Input Parameters** (read via `input()` without prompts):
   - Source file name (e.g., `mobydick.txt`)
   - Hash table size `M` (number of buckets)
   - Prefix size `n` (number of words per prefix)
   - Number of words to generate

2. **Text Processing**:
   - The text is tokenized into words.
   - A sliding window of `n` words is used to build string-based prefixes.
   - These prefixes are hashed using a custom hash function and stored in the `Hashtable` class.
   - Each prefix maps to a list of possible suffixes that follow it in the original text.

3. **Random Text Generation**:
   - Starts with a prefix of `n` `NONWORD`s (defined as `'@'`)
   - For each iteration, a suffix is chosen **randomly** from the list of suffixes associated with the current prefix.
   - The prefix window is shifted and updated accordingly.
   - A total of `k` words (as specified by the user) are generated and stored in a list.

4. **Output**:
   - The resulting list of words is printed using:
     ```python
     print(" ".join(result))
     ```

---

## 🧰 Hash Table Implementation

A custom hash table class `Hashtable` is implemented with the following interface:

```python
class Hashtable:
    def __init__(self, size)
    def put(self, key, value)
    def get(self, key)
    def __contains__(self, key)
    def __str__(self)
