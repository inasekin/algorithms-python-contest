"""
Дана последовательность натуральных чисел, завершающаяся число 0. Определите наибольшую длину монотонного фрагмента последовательности (то есть такого фрагмента, где все элементы либо больше предыдущего, либо меньше).

Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, а служит как признак ее окончания).

"""

a = int(input())
b = int(input())

max_len = 1
current_len = 1
trend = 0

while b != 0:
    if b > a:
        if trend == 1:
            current_len += 1
        else:
            current_len = 2
            trend = 1
    elif b < a:
        if trend == -1:
            current_len += 1
        else:
            current_len = 2
            trend = -1
    else:
        current_len = 1
        trend = 0

    if current_len > max_len:
        max_len = current_len

    a = b
    b = int(input())

print(max_len)