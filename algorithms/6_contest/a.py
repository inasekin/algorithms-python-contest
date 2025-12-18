n = int(input())

if n == 0 or n == 1:
    print(1)
else:
    prev = 1
    curr = 1
    for i in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10
    print(curr)
