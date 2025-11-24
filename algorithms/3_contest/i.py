# Кассы
#
# Задача: найти суммарное время, когда все N касс работают одновременно
#
# Алгоритм O(N log N) с использованием sweep line:
# 1. Для каждой кассы создаем события открытия и закрытия
# 2. Если касса работает круглосуточно (open == close), она работает [0, 86400)
# 3. Если касса работает через полночь (open > close), создаем события для [0, close) и [open, 86400)
# 4. Сортируем все события и обрабатываем их, отслеживая количество активных касс
# 5. Суммируем время, когда количество активных касс равно N

n = int(input())
events = []

for i in range(n):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    open_time = h1 * 3600 + m1 * 60 + s1
    close_time = h2 * 3600 + m2 * 60 + s2

    if open_time == close_time:
        # Круглосуточно
        events.append((0, 1))
        events.append((86400, -1))
    elif open_time < close_time:
        # Обычный случай
        events.append((open_time, 1))
        events.append((close_time, -1))
    else:
        # Через полночь: работает [0, close) и [open, 86400)
        events.append((0, 1))
        events.append((close_time, -1))
        events.append((open_time, 1))
        events.append((86400, -1))

# Сортируем события по времени
events.sort()

active_count = 0
last_time = 0
total_time = 0

for time, delta in events:
    # Если все кассы активны, добавляем прошедшее время
    if active_count == n:
        total_time += time - last_time
    active_count += delta
    last_time = time

print(total_time)