"""
Даны два натуральных числа nn и mm. Сократите дробь n/m, то есть выведите два других числа p и q таких, что n/m=p/q и дробь p/q — несократимая. Решение оформите в виде функции ReduceFraction(n, m), получающая значения n и m и возвращающей кортеж из двух чисел.
"""

n = int(input())
m = int(input())


def reduceFrac(n, m):
    a, b = n, m
    while b:
        a, b = b, a % b
    g = a
    return print(n // g, m // g)


reduceFrac(n, m)