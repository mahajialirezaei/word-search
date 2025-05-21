import collections

found_words = []
def check(i, j, m, n, visited):
    return i < m and j < n and i > 0 and j > 0 and [i, j] not in visited


def wordSearch(board, i, j, words, m, n, word, visited):
    if word in words:
        found_words.append(word)

    if check(i + 1, j, m, n, visited):
        word = word + board[i+1][j]
        visited.add([i + 1, j])
        wordSearch(board, i + 1, j, words, m, n, word, visited)
        visited.remove([i + 1, j])
    if check(i, j + 1, m, n, visited):
        word = word + board[i][j+1]
        visited.add([i, j + 1])
        wordSearch(board, i, j + 1, words, m, n, word, visited)
        visited.remove([i, j + 1])
        visited.add([i, j + 1])
    if check(i - 1, j, m, n, visited):
        word = word + board[i-1][j]
        visited.add([i - 1, j])
        wordSearch(board, i - 1, j, words, m, n, word, visited)
        visited.remove([i - 1, j])
    if check(i, j - 1, m, n, visited):
        word = word + board[i][j-1]
        visited.add([i, j - 1])
        wordSearch(board, i, j - 1, words, m, n, word, visited)
        visited.remove([i, j - 1])

