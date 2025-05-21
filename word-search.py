import collections
from os import remove

found_words = []
def check(i, j, m, n, visited):
    return i < m and j < n and i > 0 and j > 0 and [i, j] not in visited


def search(board, words, m, n):
    visited = set()
    word = ''
    for i in range(m):
        for j in range(n):
            visited.add([i, j])
            word = board[i][j]
            wordSearch(board, i, j, words, m, n, word, visited)



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



board = [
['o', 'a', 'a', 'n'],
['e', 't', 'a', 'e'],
['i', 'h', 'k', 'r'],
['i', 'f', 'l', 'v']
]

words = ['oath', 'pea', 'eat', 'rain']


m = 4
n = 4
search(board, words, m, n)
