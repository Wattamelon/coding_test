import sys
input = sys.stdin.readline

n , m = map(int,input().split())
nums = list(map(int,input().split()))
for i in range(1,len(nums)):
    nums[i] += nums[i-1]
out = []

for _ in range(m):
    start , end = map(int,input().split())
    if start == 1:
        out.append(str(nums[end-1]))
    else:
        res = nums[end-1] - nums[start-2]
        out.append(str(res))

sys.stdout.write("\n".join(out))