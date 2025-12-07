m, n = map(int, input().split())
helpers = []
max_time = 0

for _ in range(n):
    t, z, y = map(int, input().split())
    helpers.append((t, z, y))
    max_time = max(max_time, t * z + y)

l = 0
r = m * max_time

while l < r:
    mid = (l + r) // 2
    cnt = 0

    for t, z, y in helpers:
        c = z * t + y
        cnt += (mid // c) * z + min(z, (mid % c) // t)

    if cnt >= m:
        r = mid
    else:
        l = mid + 1

ans = []
need = m

for t, z, y in helpers:
    c = z * t + y
    can = (l // c) * z + min(z, (l % c) // t)
    take = min(need, can)
    ans.append(take)
    need -= take

print(l)
print(*ans)