"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 11 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.

Ввод
10 3
8 10
2 5
3 6

Вывод
I.....I...

Ввод
10 3
3 5
4 6
10 10

Вывод
II....III.

"""

f = open('input.txt', 'r')
n, k = map(int, f.readline().split())

pins = [True] * (n + 1)

for _ in range(k):
    l, r = map(int, f.readline().split())
    for i in range(l, r + 1):
        pins[i] = False

f.close()

result = ""
for i in range(1, n + 1):
    if pins[i]:
        result += "I"
    else:
        result += "."

print(result)