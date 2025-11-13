"""
Возводить в степень можно гораздо быстрее, чем за nn умножений! Для этого нужно воспользоваться следующими рекуррентными соотношениями: an=(a2)n/2an=(a2)n/2 при четном nn, an=a⋅an−1an=a⋅an−1 при нечетном nn. Реализуйте алгоритм быстрого возведения в степень. Если вы все сделаете правильно, то сложность вашего алгоритма будет O(logn)O(logn).
Формат ввода

Вводится действительное число a и целое число n.
Формат вывода

Выведите ответ на задачу.
"""

a = float(input())
n = int(input())


def exponentiation(a, n):
    if n == 0:
        return 1

    if n < 0:
        return 1.0 / exponentiation(a, -n)

    result = 1
    base = a

    while n > 0:
        if n & 1:
            result *= base
        base *= base
        n >>= 1

    return result


result = exponentiation(a, n)

if result == int(result):
    print(int(result))
else:
    print(result)