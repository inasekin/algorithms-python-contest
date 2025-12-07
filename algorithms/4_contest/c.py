n, x, y = map(int, input().split())

left, right = 0, n * max(x, y)

while left < right:
    mid = (left + right) // 2

    if mid < min(x, y):
        can_make = False
    else:
        remaining = mid - min(x, y)
        copies = 1 + remaining // x + remaining // y
        can_make = (copies >= n)

    if can_make:
        right = mid
    else:
        left = mid + 1

print(left)