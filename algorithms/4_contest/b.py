# Приближенный двоичный поиск

from bisect import bisect_left

n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for x in queries:
    pos = bisect_left(arr, x)

    # Проверяем соседние элементы
    candidates = []

    if pos < n:
        candidates.append(arr[pos])
    if pos > 0:
        candidates.append(arr[pos - 1])

    # Находим ближайший (при равном расстоянии - меньший)
    best = min(candidates, key=lambda val: (abs(val - x), val))
    print(best)