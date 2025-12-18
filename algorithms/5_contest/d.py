# Задача D. Все правильные скобочные последовательности
# Решение через итеративный подход со стеком
# Подход: генерируем все правильные скобочные последовательности
# Используем стек для хранения состояний (текущая строка, кол-во открытых, кол-во закрытых)
# На каждом шаге добавляем открывающую скобку если можем, или закрывающую если можем

n = int(input())

stack = [('', 0, 0)]
result = []

while stack:
    current, open_count, close_count = stack.pop()

    if open_count == n and close_count == n:
        result.append(current)
        continue

    if close_count < open_count:
        stack.append((current + ')', open_count, close_count + 1))

    if open_count < n:
        stack.append((current + '(', open_count + 1, close_count))

for seq in result:
    print(seq)