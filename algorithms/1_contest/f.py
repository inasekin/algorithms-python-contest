# Напишите программу, определяющую k-е по величине простое число.

# В этом коде используются следующие алгоритмы и подходы:
#
#     Решето Эратосфена (Sieve of Eratosthenes)
#         Классический алгоритм для нахождения всех простых чисел до заданного предела.
#         Создается массив is_prime[], где is_prime[i] = True означает, что i - простое число.
#         Алгоритм последовательно "вычеркивает" все составные числа (кратные простых).
#         Начинаем с p=2 и для каждого простого p вычеркиваем все кратные начиная с p².
#     Прямой доступ по индексу
#         После сбора всех простых в список, k-е простое берется как primes[k-1].
#
# Кратко: Код использует решето Эратосфена для генерации простых чисел,
# собирает их в список, затем отвечает на запросы по индексу.

limit = 2000000
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

p = 2
while p * p <= limit:
    if is_prime[p]:
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False
    p += 1

primes = []
for num in range(2, limit + 1):
    if is_prime[num]:
        primes.append(num)

n = int(input())
queries = list(map(int, input().split()))

result = []
for k in queries:
    result.append(primes[k - 1])

print(" ".join(map(str, result)))