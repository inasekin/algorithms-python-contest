"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего (с учетом регистра, и следующих знаков пунктуации за ним – не удаляйте их, и не приводите строку к нижнему регистру). Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
Формат ввода

Вводится текст.
Формат вывода

Выведите ответ на задачу.
Пример 1
Ввод
Вывод

apple orange banana banana orange

banana

Пример 2
Ввод
Вывод

oh you touch my tralala mmm my ding ding dong

ding

Пример 3
Ввод
Вывод

q w e r t y u i o p
a s d f g h j k l
z x c v b n m

a

"""

with open("input.txt", "r") as file:
    words = file.read().split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

max_freq = max(frequency.values()) if frequency else 0

most_common_words = [word for word, freq in frequency.items() if freq == max_freq]

if most_common_words:
    print(min(most_common_words))