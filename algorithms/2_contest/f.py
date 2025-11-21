"""
Задача: Гистограмма

Дана гистограмма из N прямоугольников одинаковой ширины 1.
Нужно найти площадь наибольшего прямоугольника, который полностью
лежит на общей базовой линии и вписан в гистограмму.

Решение:
Используется алгоритм со стеком за O(n).
Идея: для каждого прямоугольника находим максимальную ширину,
на которой он может быть самым низким.

Алгоритм:
1. Добавляем граничные нули слева и справа для упрощения обработки краев
2. Проходим по всем высотам слева направо
3. Поддерживаем стек индексов в порядке возрастания высот
4. Когда встречаем высоту меньше вершины стека:
   - Извлекаем индекс из стека
   - Вычисляем площадь прямоугольника с этой высотой
   - Ширина = текущая позиция - позиция предыдущего элемента стека - 1
5. Максимальная из всех вычисленных площадей - ответ

Пример: высоты [2, 1, 4, 5, 1, 3, 3]
Наибольший прямоугольник: высота 4, ширина 2 (позиции 4 и 5) → площадь 8
"""

num_rectangles = int(input())
histogram_heights = [0] + list(map(int, input().split())) + [0]
index_stack = [0]
max_rectangle_area = 0

for current_index in range(1, len(histogram_heights)):
    while histogram_heights[index_stack[-1]] > histogram_heights[current_index]:
        height_index = index_stack.pop()
        current_height = histogram_heights[height_index]
        rectangle_width = current_index - index_stack[-1] - 1
        max_rectangle_area = max(max_rectangle_area, current_height * rectangle_width)

    index_stack.append(current_index)

print(max_rectangle_area)