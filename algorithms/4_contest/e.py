a, b, c, d = map(int, input().split())

def f(x):
    return a * x**3 + b * x**2 + c * x + d

# Бинарный поиск корня
left, right = -1000.0, 1000.0

# Расширяем границы, если корень снаружи
while f(left) * f(right) > 0:
    left *= 2
    right *= 2

# Бисекция с высокой точностью
for _ in range(100):
    mid = (left + right) / 2
    if f(mid) * f(left) <= 0:
        right = mid
    else:
        left = mid

print(f"{mid:.4f}")