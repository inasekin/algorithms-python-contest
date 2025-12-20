"""
Задача о банкомате - классическая задача о размене монет (coin change).

Идея решения:
- Используем динамическое программирование
- dp[i] = минимальное количество купюр для суммы i
- Для каждой суммы от 1 до S перебираем все номиналы и выбираем вариант с минимумом купюр
- Дополнительно сохраняем parent[i] - какой номинал использовали для получения суммы i
- Это позволит восстановить сам набор купюр в конце

Сложность: O(S * N), где S - нужная сумма, N - количество номиналов
"""

n = int(input())
denominations = list(map(int, input().split()))
s = int(input())

dp = [float('inf')] * (s + 1)
dp[0] = 0
parent = [-1] * (s + 1)

for i in range(1, s + 1):
    for denom in denominations:
        if denom <= i and dp[i - denom] + 1 < dp[i]:
            dp[i] = dp[i - denom] + 1
            parent[i] = denom

if dp[s] == float('inf'):
    print(-1)
else:
    print(dp[s])

    result = []
    current = s
    while current > 0:
        denom = parent[current]
        result.append(denom)
        current -= denom

    result.reverse()

    print(' '.join(map(str, result)))