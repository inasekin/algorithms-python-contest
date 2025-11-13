"""
Напишите программу, которая представляет переданное натуральное число в виде суммы не более чем 7 кубов других натуральных чисел.
Формат ввода

Входная строка содержит целое число

N

, которое нужно представить в виде суммы кубов.
Формат вывода

Программа должна вывести любое разложение переданного ей числа в виде суммы не более чем 7 кубов других натуральных чисел. Если такое разложение невозможно, программа должна вывести число 0.

"""

n = int(input())
MAX_K = 7

def icbrt(x: int) -> int:
    lo, hi = 0, 1
    while hi * hi * hi <= x:
        hi <<= 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid * mid <= x:
            lo = mid
        else:
            hi = mid
    return lo

ans = []

def dfs(rem, k, max_base, cur):
    if rem == 0:
        global ans
        ans = cur[:]
        return True
    if k == 0 or max_base == 0:
        return False

    m = min(max_base, icbrt(rem))
    for a in range(m, 0, -1):
        cube = a * a * a
        if cube > rem:
            continue
        if dfs(rem - cube, k - 1, a, cur + [a]):
            return True
    return False

dfs(n, MAX_K, icbrt(n), [])

if ans:
    print(*[x * x * x for x in ans])
else:
    print(0)