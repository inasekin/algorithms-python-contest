t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    mustAttend = 0
    skipped = 0

    for i in range(n):
        if mustAttend > 0:
            mustAttend -= 1
        elif s[i] == '0':
            skipped += 1

        if s[i] == '1':
            mustAttend = k

    print(skipped)