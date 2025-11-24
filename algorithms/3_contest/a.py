# Непрерывный рюкзак
#
# Задача о дробном рюкзаке (fractional knapsack)
# Нужно максимизировать стоимость предметов в рюкзаке вместимостью W,
# при этом можно брать дробные части предметов
#
# Жадный алгоритм за O(N log N):
# 1. Вычисляем удельную стоимость каждого предмета (стоимость/объем)
# 2. Сортируем предметы по убыванию удельной стоимости
# 3. Жадно берем предметы с наибольшей удельной стоимостью
# 4. Если предмет не влезает целиком, берем его часть

n, W = map(int, input().split())

items = []
for i in range(n):
    c, w = map(int, input().split())
    # Сохраняем: (удельная стоимость, стоимость, объем)
    items.append((c / w, c, w))

# Сортируем по убыванию удельной стоимости
items.sort(reverse=True)

total_value = 0.0  # Суммарная стоимость
remaining_capacity = W  # Оставшееся место в рюкзаке

for unit_value, cost, weight in items:
    if remaining_capacity == 0:
        break

    if weight <= remaining_capacity:
        # Берем предмет целиком
        total_value += cost
        remaining_capacity -= weight
    else:
        # Берем часть предмета
        fraction = remaining_capacity / weight
        total_value += cost * fraction
        remaining_capacity = 0

# Выводим с точностью не менее 3 знаков после запятой
print(f"{total_value:.3f}")