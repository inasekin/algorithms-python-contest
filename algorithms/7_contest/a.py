S, N = map(int, input().split())
weights = list(map(int, input().split()))

# Создаем массив dp, где dp[i] - максимальный вес для вместимости i
dp = [0] * (S + 1)

# Для каждого слитка
for w in weights:
    # Проходим в обратном порядке, чтобы не использовать слиток дважды
    for capacity in range(S, w - 1, -1):
        dp[capacity] = max(dp[capacity], dp[capacity - w] + w)

# Вывод результата
print(dp[S])