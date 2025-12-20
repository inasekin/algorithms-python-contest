# Чтение входных данных
N = int(input())
masses = list(map(int, input().split()))

# Считаем общую сумму
total = sum(masses)

# Если сумма нечётная, разделить невозможно
if total % 2 != 0:
    print("NO")
else:
    # Нужно проверить, можно ли набрать половину суммы
    target = total // 2

    # dp[i] = True, если можно набрать сумму i
    dp = [False] * (target + 1)
    dp[0] = True  # Сумму 0 можно набрать (не берём ничего)

    # Для каждой гири
    for mass in masses:
        # Проходим в обратном порядке
        for weight in range(target, mass - 1, -1):
            if dp[weight - mass]:
                dp[weight] = True

    # Проверяем, можно ли набрать target
    if dp[target]:
        print("YES")
    else:
        print("NO")