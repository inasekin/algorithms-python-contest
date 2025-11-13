"""
Дано натуральное число n>1n>1. Выведите его наименьший делитель, отличный от 1. Алгоритм должен иметь сложность O(√n). Указание. Если у числа nn нет делителя не превосходящего √n , то число n — простое и ответом будет само число nn.
"""

n = int(input())

def find_divisor(n):
    if n % 2 == 0:
        return 2

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 2

    return n

print(find_divisor(n))