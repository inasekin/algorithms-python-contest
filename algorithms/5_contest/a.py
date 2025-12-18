# Задача A. Разбиение на неубывающие слагаемые, обратный порядок
# Решение через итеративный подход со стеком
# Подход: генерируем все разбиения числа N на натуральные слагаемые
# Используем стек для обхода всех возможных вариантов разбиения
# Каждое слагаемое не меньше предыдущего (неубывающая последовательность)
# В конце разворачиваем список разбиений для вывода в обратном порядке

n = int(input())
result = []
stack = [(n, [], 1)]

while stack:
    remaining, current, min_val = stack.pop()

    if remaining == 0:
        result.append(current[:])
        continue

    for i in range(min_val, remaining + 1):
        stack.append((remaining - i, current + [i], i))

for part in result:
    print(' '.join(map(str, part)))