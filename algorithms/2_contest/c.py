"""
Вычисление выражений в постфиксной записи (обратная польская нотация).

Проверяем корректность:
- Пустое выражение
- Недостаточно операндов
- Деление на 0
- Переполнение диапазона [-2^63, 2^63-1]
- В конце должен быть ровно 1 элемент

Сложность: O(n)
"""

n = int(input())

MIN_VAL = -(2 ** 63)
MAX_VAL = 2 ** 63 - 1

if n == 0:
    print("Incorrect String!")
else:
    tokens = input().split()

    stack = []
    valid = True

    for token in tokens:
        if token == '+':
            if len(stack) < 2:
                valid = False
                break
            b = stack.pop()
            a = stack.pop()
            result = a + b
            if result < MIN_VAL or result > MAX_VAL:
                valid = False
                break
            stack.append(result)
        elif token == '-':
            if len(stack) < 2:
                valid = False
                break
            b = stack.pop()
            a = stack.pop()
            result = a - b
            if result < MIN_VAL or result > MAX_VAL:
                valid = False
                break
            stack.append(result)
        elif token == '*':
            if len(stack) < 2:
                valid = False
                break
            b = stack.pop()
            a = stack.pop()
            result = a * b
            if result < MIN_VAL or result > MAX_VAL:
                valid = False
                break
            stack.append(result)
        elif token == '/':
            if len(stack) < 2:
                valid = False
                break
            b = stack.pop()
            a = stack.pop()
            if b == 0:
                valid = False
                break
            result = int(a / b)
            if result < MIN_VAL or result > MAX_VAL:
                valid = False
                break
            stack.append(result)
        else:
            try:
                num = int(token)
                stack.append(num)
            except:
                valid = False
                break

    if valid and len(stack) == 1:
        print(stack[0])
    else:
        print("Incorrect String!")