"""
Partition element
Алгоритм partition разбивает массив на две части относительно опорного элемента x:
- Элементы < x идут в левую часть
- Элементы >= x идут в правую часть
Это базовая операция для быстрой сортировки (QuickSort)
"""

n = int(input())
arr_line = input()
if n > 0:
    arr = list(map(int, arr_line.split()))
else:
    arr = []
x = int(input())

less_count = sum(1 for elem in arr if elem < x)
greater_or_equal_count = n - less_count

print(less_count)
print(greater_or_equal_count)