# Чтение входных данных
N, M = map(int, input().split())
masses = list(map(int, input().split()))

# dp[i] = минимальное количество предметов для набора веса i
# Используем большое число как "бесконечность"
INF = float('inf')
dp = [INF] * (M + 1)
dp[0] = 0  # Для веса 0 нужно 0 предметов

# Для каждого предмета
for mass in masses:
    # Проходим в обратном порядке
    for weight in range(M, mass - 1, -1):
        if dp[weight - mass] != INF:
            dp[weight] = min(dp[weight], dp[weight - mass] + 1)

# Вывод результата
if dp[M] == INF:
    print(0)
else:
    print(dp[M])