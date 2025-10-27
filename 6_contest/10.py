"""
Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys) записан текст. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите, сколько различных слов содержится в этом тексте.
Формат ввода

Вводится текст.
Формат вывода

Выведите ответ на задачу.
Пример
Ввод
Вывод

She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.



19

"""

import sys

def solve():
    words = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        words.extend(line.split())

    if not words:
        print(0)
        return

    words.sort()
    count = 1
    for i in range(1, len(words)):
        if words[i] != words[i - 1]:
            count += 1

    print(count)

solve()