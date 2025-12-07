t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    prefix = [0]
    for val in a:
        prefix.append(prefix[-1] + val)

    MAXLOG = 40
    jump = [[n] * MAXLOG for _ in range(n + 1)]

    for i in range(n):
        for bit in range(MAXLOG):
            threshold = 1 << bit
            left, right = i + 1, n + 1
            while left < right:
                mid = (left + right) // 2
                if prefix[mid] - prefix[i] < threshold:
                    left = mid + 1
                else:
                    right = mid
            jump[i][bit] = left

    for _ in range(q):
        l, r, x = map(int, input().split())
        l -= 1

        clears = 0
        pos = l

        for bit in range(MAXLOG - 1, -1, -1):
            if (1 << bit) <= x and jump[pos][bit] <= r:
                x -= (1 << bit)
                pos = jump[pos][bit]
                clears += 1

        print(clears, prefix[r] - prefix[pos])