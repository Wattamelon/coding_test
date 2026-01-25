# 다른 로직(판별 방식 유지) - 네 방식 개선 버전
# 개별 수마다 sqrt까지 나눠보는 방식(체보다 느리지만 구현은 단순)

import sys
input = sys.stdin.readline

m, n = map(int, input().split())

def is_prime_num(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    r = int(x ** 0.5)
    for d in range(3, r + 1, 2):
        if x % d == 0:
            return False
    return True

out = []
for x in range(m, n + 1):
    if is_prime_num(x):
        out.append(str(x))

sys.stdout.write("\n".join(out))
