n, k = map(int, input().split())
points = list(map(int, input().split()))

points.sort()

l = 0
r = points[-1] - points[0]

while l < r:
    mid = (l + r) // 2

    cnt = 1
    start = points[0]

    for i in range(1, n):
        if points[i] - start > mid:
            cnt += 1
            start = points[i]

    if cnt <= k:
        r = mid
    else:
        l = mid + 1

print(l)