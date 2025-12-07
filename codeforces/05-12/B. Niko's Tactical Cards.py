t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    minVal = 0
    maxVal = 0

    for i in range(n):
        opt1Min = minVal - a[i]
        opt1Max = maxVal - a[i]
        opt2Min = b[i] - maxVal
        opt2Max = b[i] - minVal

        minVal = min(opt1Min, opt2Min)
        maxVal = max(opt1Max, opt2Max)

    print(maxVal)