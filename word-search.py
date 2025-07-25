import collections
from os import remove

found_words = set()
def check(i, j, m, n, visited):
    return i < m and j < n and i >= 0 and j >= 0 and tuple([i, j]) not in visited


def search(board, words, m, n):
    word = ''
    for i in range(m):
        for j in range(n):
            visited = set()
            visited.add(tuple([i, j]))
            word = board[i][j]
            wordSearch(board, i, j, words, m, n, word, visited)




def wordSearch(board, i, j, words, m, n, word, visited):
    if word in words:
        found_words.add(word)

    if check(i + 1, j, m, n, visited):
        word = word + board[i+1][j]
        visited.add(tuple([i + 1, j]))
        wordSearch(board, i + 1, j, words, m, n, word, visited)
        visited.remove(tuple([i + 1, j]))
        word = word[:-1]
    if check(i, j + 1, m, n, visited):
        word = word + board[i][j+1]
        visited.add(tuple([i, j + 1]))
        wordSearch(board, i, j + 1, words, m, n, word, visited)
        visited.remove(tuple([i, j + 1]))
        word = word[:-1]

    if check(i - 1, j, m, n, visited):
        word = word + board[i-1][j]
        visited.add(tuple([i - 1, j]))
        wordSearch(board, i - 1, j, words, m, n, word, visited)
        visited.remove(tuple([i - 1, j]))
        word = word[:-1]

    if check(i, j - 1, m, n, visited):
        word = word + board[i][j-1]
        visited.add(tuple([i, j - 1]))
        wordSearch(board, i, j - 1, words, m, n, word, visited)
        visited.remove(tuple([i, j - 1]))
        word = word[:-1]



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


for x in found_words:
    print(x)


board = [
    ['a', 'b'],
    ['c', 'd']
]

words = ['abdc']

m = 2
n = 2
search(board, words, m, n)

for x in found_words:
    print(x)
