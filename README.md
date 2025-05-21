### 📄 `README.md`

````markdown
# Word Search in Character Grid

This project implements a classic **Word Search** algorithm in Python. The goal is to identify which words from a given list can be formed by navigating through adjacent characters in a 2D board.

> Developed by [@mahajialirezaei](https://github.com/mahajialirezaei)

## 📌 Problem Statement

Given:
- A 2D grid (`board`) of lowercase English letters (dimensions `m x n`)
- A list of words (`words`) to search

Find all words from the list that can be constructed by chaining adjacent cells on the board.

### ✅ Valid Word Path Criteria:
- Letters must be **adjacent** (horizontally or vertically — not diagonally).
- Each cell can be **used only once per word**.
- Word must be **fully contained** within the board boundaries.

---

## 🧠 Algorithm Logic

The algorithm performs a **depth-first search (DFS)** starting from every cell in the board. For each DFS path:

- It keeps track of visited cells to prevent revisiting in the same path.
- Builds potential word strings dynamically.
- If the built word exists in the given word list, it is stored as a result.
- Backtracking is used to explore alternate paths.

---

## 🧪 Example

```python
board = [
  ['o', 'a', 'a', 'n'],
  ['e', 't', 'a', 'e'],
  ['i', 'h', 'k', 'r'],
  ['i', 'f', 'l', 'v']
]

words = ['oath', 'pea', 'eat', 'rain']

# Output: ['oath', 'eat']
````

---

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/mahajialirezaei/your-repo-name.git
   cd your-repo-name
   ```

2. Run the script:

   ```bash
   python3 word_search.py
   ```

---

## 🛠 Features

* Supports multiple boards and word lists.
* Prevents duplicate word detection.
* Uses Python sets for efficient lookups.
* Clean, recursive backtracking logic.

---

## 🚀 Future Improvements

* Support for Trie-based optimization (prefix tree) to handle large word dictionaries more efficiently.
* Add unit tests for various edge cases.
* GUI for interactive board input.



---

