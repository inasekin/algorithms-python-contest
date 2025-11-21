"""
Задача о минимальном отрезке аллеи, содержащем все виды деревьев.

Используем алгоритм скользящего окна (two pointers).
Двигаем правую границу, пока не соберем все виды,
затем сжимаем окно слева, пока можем.

Сложность: O(N) времени, O(K) памяти
"""

n, k = map(int, input().split())
colors = list(map(int, input().split()))

left = 0
color_count = {}
unique_colors = 0

min_length = n + 1
best_left = 0
best_right = 0

for right in range(n):
    color = colors[right]
    if color not in color_count:
        color_count[color] = 0
    color_count[color] += 1

    if color_count[color] == 1:
        unique_colors += 1

    while unique_colors == k:
        length = right - left + 1
        if length < min_length:
            min_length = length
            best_left = left
            best_right = right

        left_color = colors[left]
        color_count[left_color] -= 1
        if color_count[left_color] == 0:
            unique_colors -= 1
        left += 1

print(best_left + 1, best_right + 1)