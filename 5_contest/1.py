"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет - не выводите ничего. Если таких пар соседей несколько - выведите первую пару.

Ввод
-1 2 3 -1 -2

Вывод
2 3

"""
def neighbors() -> str:
    var = input().split()
    result = []
    for i in range(len(var) - 1):
        current = int(var[i])
        next_val = int(var[i + 1])
        if (current > 0 and next_val > 0) or (current < 0 and next_val < 0):
            result.append(current)
            result.append(next_val)
            break

    print(" ".join(map(str, result)))

neighbors()