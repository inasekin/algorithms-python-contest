# Бинпоиск

from bisect import bisect_left

n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for x in queries:
    # Бинарный поиск: находим позицию, куда вставился бы элемент x
    pos = bisect_left(arr, x)

    # Проверяем: если позиция в пределах массива и элемент на этой позиции равен x
    if pos < n and arr[pos] == x:
        print("YES")
    else:
        print("NO")