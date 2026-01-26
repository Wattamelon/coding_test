# solution_byGPT.py
# BOJ 1929 소수 구하기 - 에라토스테네스의 체 (정석/최적)

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

# i*i <= n까지만 지우면 됨
limit = int(n ** 0.5)
for i in range(2, limit + 1):
    if is_prime[i]:
        start = i * i
        step = i
        is_prime[start:n + 1:step] = [False] * (((n - start) // step) + 1)
        

out = []
for x in range(m, n + 1):
    if is_prime[x]:
        out.append(str(x))

sys.stdout.write("\n".join(out))
