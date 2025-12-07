t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    aSet = set(a)
    maxA = max(a)

    candidates = set()
    for x in aSet:
        i = 1
        while i * i <= x:
            if x % i == 0:
                if i <= k:
                    candidates.add(i)
                if x // i <= k:
                    candidates.add(x // i)
            i += 1

    valid = []
    for b in sorted(candidates):
        if b > maxA:
            continue

        isValid = True
        mult = b
        while mult <= min(k, maxA):
            if mult not in aSet:
                isValid = False
                break
            mult += b

        if isValid and mult > k:
            valid.append(b)

    if not valid:
        print(-1)
        continue

    result = set()
    for x in aSet:
        for b in valid:
            if x % b == 0:
                result.add(b)
                break

    print(len(result))
    print(*sorted(result))