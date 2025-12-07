n, s = map(int, input().split())
m = []
for _ in range(n):
    a, b, c = map(int, input().split())
    m.append((a, b, c))

thresholds = sorted(set([0] + [c for _, _, c in m if c <= n]), reverse=True)

ans = 0
for i in range(len(thresholds)):
    k_max = thresholds[i]
    k_min = thresholds[i + 1] if i + 1 < len(thresholds) else 0

    agg = sorted([a if k_max <= c else b for a, b, c in m])

    for k in range(min(k_max, n), k_min, -1):
        if sum(agg[:k]) <= s:
            ans = k
            break

    if ans > 0:
        break

print(ans)