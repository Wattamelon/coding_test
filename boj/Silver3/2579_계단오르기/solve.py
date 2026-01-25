import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort(reverse = True)
dp = nums[0]
i = n-2
cnt = 1
while i > 0:
    if nums[i-1] > nums[i-2]:
        dp += nums[i]

