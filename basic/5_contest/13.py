"""
Даны два списка чисел, которые могут содержать до 10000 чисел каждый. Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания. Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
Формат ввода

Вводятся два списка целых чисел. Все числа каждого списка находятся на отдельной строке.
Формат вывода

Выведите ответ на задачу.

Ввод
1 3 2
4 3 2

Вывод
2 3
"""

def m():
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            if len(result) == 0 or result[-1] != list1[i]:
                result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    print(' '.join(map(str, result)))

m()