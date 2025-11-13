"""
В данном списке из n≤10^5 целых чисел найдите три числа,произведение которых максимально.

Решение должно иметь сложность O(n), где nn - размер списка.

Выведите три искомых числа в любом порядке.

Ввод
-5 -30000 -12
Вывод
-5 -12 -30000

Ввод
3 5 1 7 9 0 9 -3 10
Вывод
10 9 9

"""

f = open('input.txt', 'r')
numbers = list(map(int, f.readline().split()))
f.close()

max1 = max2 = max3 = float('-inf')
min1 = min2 = float('inf')

for num in numbers:
    if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num > max2:
        max3 = max2
        max2 = num
    elif num > max3:
        max3 = num

    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num

prod1 = max1 * max2 * max3
prod2 = min1 * min2 * max1

if prod1 > prod2:
    print(max1, max2, max3)
else:
    print(max1, min1, min2)