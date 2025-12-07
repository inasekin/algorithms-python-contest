n, k = map(int, input().split())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

left, right = 1, max(ropes)
result = 0

while left <= right:
    mid = (left + right) // 2

    # Считаем сколько веревок длины mid можно нарезать
    count = sum(rope // mid for rope in ropes)

    if count >= k:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)