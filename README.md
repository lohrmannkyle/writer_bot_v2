# ✍️ Writer Bot (Markov Chain Text Generator)

`writer_bot_ht.py` is a Python program that generates random text using a Markov chain algorithm based on a given source text. It builds a prefix-to-suffix mapping using a hash table to efficiently simulate language patterns.

---

## 📌 Program Overview

The program:
1. Reads a source text file.
2. Constructs a hash table mapping prefixes to suffixes.
3. Generates a specified number of random words based on the Markov chain model.
4. Prints the generated text in the desired output format.

---

## 📥 Inputs

The program expects **four inputs** from the user, read using `input()` (no prompts):

1. **Source file name** (e.g., `mobydick.txt`)
2. **Hash table size** (`M`) — an integer representing the number of buckets
3. **Prefix size** (`n`) — number of words in each prefix
4. **Number of words to generate** — total number of words to output

📌 **Important**:  
- Input must be entered in the correct order.
- Do **not** hardcode any values or add prompts.

---

## 🧠 How It Works

- The source file is parsed to extract a list of words.
- Prefixes of size `n` are used as keys in a hash table, where each key maps to a list of possible suffixes.
- Starting with a random prefix, the program chooses a suffix at random from the corresponding list, appends it to the generated text, then updates the prefix window.
- This process repeats until the requested number of words has been generated.

---

## 🖨️ Output Format

The final result is a single line of randomly generated words (joined with spaces), printed using:

```python
print(" ".join(result))
