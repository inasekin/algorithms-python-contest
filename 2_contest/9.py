"""
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""

var = int(input())
count = 0

while True:
    current = int(input())
    if current == 0:
        break

    if current > var:
        count += 1

    var = current

print(count)