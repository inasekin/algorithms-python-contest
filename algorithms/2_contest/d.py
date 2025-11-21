"""
Частотный анализ текста.

Подсчитываем частоту каждого слова и выводим слова по убыванию частоты.
При одинаковой частоте - в лексикографическом порядке.

Сложность: O(n + k log k), где n - количество слов, k - уникальных слов
"""

import sys

text = sys.stdin.read()
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word)