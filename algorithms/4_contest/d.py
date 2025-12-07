n = int(input())
arr = list(map(int, input().split()))
m = int(input())

# Находим индексы всех нулевых элементов
zero_indices = []
for i in range(n):
    if arr[i] == 0:
        zero_indices.append(i + 1)

# Отвечаем на запросы
result = []
for _ in range(m):
    k = int(input())
    if k <= len(zero_indices):
        result.append(zero_indices[k - 1])
    else:
        result.append(-1)

print(' '.join(map(str, result)))