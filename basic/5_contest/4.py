"""
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
Формат ввода

Вводится список чисел. Все числа списка находятся на одной строке.
Формат вывода

Выведите ответ на задачу.

Ввод
1 2 2 3 3 3

Вывод
3
"""

def d():
    vars_list = input().split()
    result = []

    for i in range(len(vars_list)):
        if vars_list[i] in result:
            continue
        else:
            result.append(vars_list[i])

    print(len(result))

d()