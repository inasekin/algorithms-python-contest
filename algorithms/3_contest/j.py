# Проблема тимлида
#
# Решение за O(N log N) с использованием бинарного поиска
# Идея: для каждого интервала [s, t] находим количество других интервалов, которые с ним пересекаются
#
# Ключевое наблюдение:
# Интервал [s₁, t₁] пересекается с [s, t], если:
# - s₁ <= t (сотрудник пришел не позже, чем текущий ушел)
# - t₁ >= s (сотрудник ушел не раньше, чем текущий пришел)
#
# Формула: количество_пересечений = (пришедшие_не_позже_t) - (ушедшие_раньше_s) - 1

n = int(input())
intervals = []
for i in range(n):
    s, t = map(int, input().split())
    intervals.append((s, t))

# Создаем отсортированные массивы всех времен прихода и ухода
starts = [s for s, t in intervals]
ends = [t for s, t in intervals]

starts.sort()
ends.sort()

result = []
for s, t in intervals:
    # Бинарный поиск: сколько сотрудников пришло не позже времени t
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if starts[mid] <= t:
            left = mid + 1
        else:
            right = mid - 1
    count_starts = left  # количество сотрудников с start <= t

    # Бинарный поиск: сколько сотрудников ушло раньше времени s
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if ends[mid] < s:
            left = mid + 1
        else:
            right = mid - 1
    count_ends = left  # количество сотрудников с end < s

    # Количество пересечений = (пришли не позже t) - (ушли раньше s) - 1 (сам)
    # Вычитаем 1, чтобы не считать самого себя
    result.append(count_starts - count_ends - 1)

for num in result:
    print(num)