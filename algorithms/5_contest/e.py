a, b, c, d = map(int, input().split())

stack = [[float(a), float(b), float(c), float(d)]]
ok = False

while stack and not ok:
    nums = stack.pop()

    if len(nums) == 1:
        if abs(nums[0] - 24.0) < 1e-6:
            ok = True
        continue

    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            x = nums[i]
            y = nums[j]

            rest = [nums[k] for k in range(n) if k != i and k != j]

            candidates = [
                x + y,
                x - y,
                y - x,
                x * y,
            ]

            if abs(y) > 1e-9:
                candidates.append(x / y)
            if abs(x) > 1e-9:
                candidates.append(y / x)

            for v in candidates:
                stack.append(rest + [v])

print("YES" if ok else "NO")