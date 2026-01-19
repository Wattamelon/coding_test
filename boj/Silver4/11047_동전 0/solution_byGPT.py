import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0
for c in reversed(coins):  # 입력이 오름차순이라 뒤에서부터(큰 동전부터)
    if k == 0:
        break
    cnt += k // c
    k %= c

print(cnt)
