import sys

input = sys.stdin.readline


def solve():
    x = int(input())
    if x == 1:
        print(0)
        return

    # 1. 미리 필요한 크기만큼 할당 (Pre-allocation)
    dp = [0] * (x + 1)

    for i in range(2, x + 1):
        # 2. 기본값: 1을 빼는 경우
        dp[i] = dp[i - 1] + 1

        # 3. 나누기 연산은 '나누어 떨어질 때'만 비교
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[x])


solve()