"""
По данным числам nn и kk (0≤k≤n)(0≤k≤n) вычислите СknСnk​. Для решения используйте рекуррентное соотношение Ckn=Ck−1n−1+Ckn−1Cnk​=Cn−1k−1​+Cn−1k​. Решение оформите в виде функции C(n, k).
"""

n,k = int(input()), int(input())
def solve(n, k):
    return 1 if k == 0 or k == n else solve(n - 1, k - 1) + solve(n - 1, k)
print(solve(n,k))