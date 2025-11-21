"""
Задача о наибольшем прямоугольнике в гистограмме.

Алгоритм: для каждого столбца находим левую и правую границы,
где высота становится меньше текущей. Площадь = высота × ширину.

Сложность: O(n) времени, O(n) памяти
"""

data = list(map(int, input().split()))
n = data[0]
heights = data[1:n+1]

right_border = [n] * n
stack = []

for i in range(n):
    while stack and heights[i] < heights[stack[-1]]:
        idx = stack.pop()
        right_border[idx] = i
    stack.append(i)

left_border = [-1] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and heights[i] < heights[stack[-1]]:
        idx = stack.pop()
        left_border[idx] = i
    stack.append(i)

max_area = 0
for i in range(n):
    width = right_border[i] - left_border[i] - 1
    area = heights[i] * width
    max_area = max(max_area, area)

print(max_area)