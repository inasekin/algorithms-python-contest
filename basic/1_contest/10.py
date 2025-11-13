"""
Пирожок в столовой стоит AA рублей и BB копеек. Определите, сколько рублей и копеек нужно заплатить за NN пирожков.
Формат ввода

Программа получает на вход три числа: AA, BB, NN — целые, неотрицательные, не превышают 10000.
Формат вывода

Программа должна вывести два числа: стоимость покупки в рублях и копейках.
"""

rubInput = int(input())
kopecksInput = int(input())
quantity = int(input())

rubFromKopecks = (kopecksInput * quantity) // 100

print(rubInput * quantity + rubFromKopecks, end=" ")
print((kopecksInput * quantity) % 100)