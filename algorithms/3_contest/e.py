# Костюмы
#
# Задача: максимизировать суммарную скорость команды при раздаче костюмов
#
# Ключевая идея:
# 1. Процентные костюмы дают разный бонус в зависимости от базовой скорости игрока
# 2. Фиксированные костюмы дают одинаковый бонус любому игроку
# 3. Нужно выбрать топ-N лучших бонусов (где N - количество игроков)
#
# Алгоритм:
# 1. Сортируем игроков по убыванию скорости
# 2. Сортируем процентные костюмы по убыванию процента
# 3. Для каждого процентного костюма вычисляем бонус со своим игроком
# 4. Добавляем все фиксированные бонусы
# 5. Сортируем все бонусы по убыванию и берем топ-N
# 6. Итоговая скорость = сумма базовых скоростей + сумма выбранных бонусов

n = int(input())
speeds = list(map(int, input().split()))
k = int(input())

percent_suits = []
fixed_suits = []

# Разделяем костюмы на два типа
for _ in range(k):
    suit_type, power = map(int, input().split())
    if suit_type == 1:
        percent_suits.append(power)
    else:
        fixed_suits.append(power)

# Сортируем игроков и процентные костюмы по убыванию
speeds.sort(reverse=True)
percent_suits.sort(reverse=True)
fixed_suits.sort(reverse=True)

bonuses = []

# Вычисляем бонусы от процентных костюмов
# Лучшие проценты даем игрокам с наибольшей базовой скоростью
for i in range(min(len(percent_suits), n)):
    bonus = speeds[i] * percent_suits[i] / 100
    bonuses.append(bonus)

# Добавляем все фиксированные бонусы
for fixed in fixed_suits:
    bonuses.append(fixed)

# Сортируем все бонусы по убыванию и берем лучшие N
bonuses.sort(reverse=True)

# Суммарная скорость = базовые скорости всех игроков + топ бонусы
total_speed = sum(speeds)
for i in range(min(n, len(bonuses))):
    total_speed += bonuses[i]

print(f"{total_speed:.10f}")