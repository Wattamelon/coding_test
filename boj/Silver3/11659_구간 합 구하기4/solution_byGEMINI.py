import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 맨 앞에 0을 붙여서 입력받기
nums = [0] + list(map(int, input().split()))

# 누적 합 미리 계산 (인덱스 1부터 n까지)
for i in range(1, n + 1):
    nums[i] += nums[i-1]

out = []
for _ in range(m):
    s, e = map(int, input().split())
    # i번째부터 j번째까지 합: prefix[j] - prefix[i-1]
    # start가 1이어도 nums[0]이 0이므로 예외 처리 필요 없음!
    out.append(str(nums[e] - nums[s-1]))

sys.stdout.write("\n".join(out))