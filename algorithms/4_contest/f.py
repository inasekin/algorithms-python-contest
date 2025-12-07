n, a, b, w, h = map(int, input().split())

# Бинарный поиск по толщине защиты
left, right = 0, max(w, h)
result = 0

while left <= right:
    mid = (left + right) // 2

    # Размеры модуля с защитой
    width = a + 2 * mid
    height = b + 2 * mid

    # Вариант 1: без поворота
    count1 = (w // width) * (h // height)

    # Вариант 2: с поворотом
    count2 = (w // height) * (h // width)

    # Проверяем, можно ли разместить n модулей
    if max(count1, count2) >= n:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)