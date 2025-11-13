"""
Дан список из NN ( N≤2∗10^5) элементов,которые принимают целые значения от 0 до 100.

Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.

Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.Использовать встроенные функции сортировки нельзя.

Ввод
7 3 4 2 5

Вывод
2 3 4 5 7
"""

f = open('input.txt', 'r')
numbers = list(map(int, f.readline().split()))
f.close()


def CountSort(list):
    count = [0] * 101

    for num in list:
        count[num] += 1

    result = []
    for i in range(101):
        if count[i] > 0:
            result.extend([i] * count[i])

    print(" ".join(map(str, result)))


CountSort(numbers)