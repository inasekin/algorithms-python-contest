# Задача I. Anti-qsort test
# Генерируем перестановку для плохой работы quicksort
# Подход: строим массив итеративно через стек
# Средний элемент каждого подмассива делаем максимальным в нем

n = int(input())
result = [0] * n

stack = [(0, n - 1, 1)]

while stack:
    left, right, start_val = stack.pop()

    if left > right:
        continue

    if left == right:
        result[left] = start_val
        continue

    mid = (left + right) // 2
    size = right - left + 1
    result[mid] = start_val + size - 1

    if mid > left:
        stack.append((left, mid - 1, start_val))

    if mid < right:
        stack.append((mid + 1, right, start_val + mid - left))

print(' '.join(map(str, result)))