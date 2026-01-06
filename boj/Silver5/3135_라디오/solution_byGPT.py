import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())

ans = abs(a - b)  # 즐겨찾기 없이 이동

for _ in range(n):
    f = int(input())
    ans = min(ans, 1 + abs(f - b))  # 즐겨찾기 1번 + 이후 +/- 이동

print(ans)
