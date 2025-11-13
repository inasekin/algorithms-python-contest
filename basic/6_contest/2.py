"""
Проверьте, есть ли среди данных N чисел нули.
Формат ввода

Вводится число N, а затем N чисел.
Формат вывода

Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в противном случае.
Пример 1
Ввод
Вывод

3
4
19
14



False

Пример 2
Ввод
Вывод

7
8
8
8
12
12
11
28



False

Пример 3
Ввод
Вывод

7
0
20
9
14
5
29
4



True

"""

def solve():
	f = open('input.txt', 'r')

	f.readline()

	numbers = []
	while True:
		line = f.readline().strip()
		if line == '':
			break
		numbers.append(line)

	f.close()

	if min(map(int, numbers)) == 0:
		print(True)
	else:
		print(False)

solve()