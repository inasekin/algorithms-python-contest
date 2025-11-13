"""
Администрация области N решила оптимизировать количество школ. Известно, что все n селений находятся вдоль одной прямой дороги. Вдоль дороги также расположены m школ, в которые дети поселков ходят.

Для того, чтобы выяснить текущую загруженность школ, необходимо для каждого селения определить ближайшую к нему школу.
Формат ввода

В первой строке вводится число n - количество селений (1 <= n <= 100000). Вторая строка содержит n различных целых чисел, i-е из этих чисел задает расстояние от начала дороги до ii-го селения. В третьей строке входных данных задается число mm - количество школ (1 <= mm <= 100000). Четвертая строка содержит mm различных целых чисел, ii-е из этих чисел задает расстояние от начала дороги до ii-ой школы. Все расстояния положительны и не превышают 109109. Селение и школа могут располагаться в одной точке.
Формат вывода

Выведите n чисел - для каждого селения выведите номер ближайшей к нему школы. Школы пронумерованы от 1 до m в том порядке, в котором они заданы во входных данных.

Пример 1
Ввод
4
1 2 6 10
2
7 3
Вывод
2
2
1
1


Пример 2
Ввод
1
1
1
2
Вывод
1

Пример 3
Ввод
10
79 64 13 8 38 29 58 20 56 17
10
53 19 20 85 82 39 58 46 51 69
Вывод
5
10
2
2
6
3
7
3
7
2

"""

f = open('input.txt', 'r')

n = int(f.readline())
villages = list(map(int, f.readline().split()))
m = int(f.readline())
schools = list(map(int, f.readline().split()))

f.close()

schools_sorted = [(schools[i], i + 1) for i in range(m)]
schools_sorted.sort()

for village_pos in villages:
    left, right = 0, m - 1

    while left < right:
        mid = (left + right) // 2
        if schools_sorted[mid][0] < village_pos:
            left = mid + 1
        else:
            right = mid

    best = schools_sorted[left]
    if left > 0:
        dist_prev = abs(schools_sorted[left - 1][0] - village_pos)
        dist_curr = abs(schools_sorted[left][0] - village_pos)
        if dist_prev < dist_curr or (dist_prev == dist_curr and schools_sorted[left - 1][1] < schools_sorted[left][1]):
            best = schools_sorted[left - 1]

    print(best[1])