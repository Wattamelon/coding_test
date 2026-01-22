import sys
input = sys.stdin.readline

t = int(input())
out = []
nums = [0,1,2,4,7]

for i in range(5,12):
    nums.append(nums[i-1] + nums[i-2] + nums[i-3])
nums = list(map(str,nums))

for _ in range(t):
    num = int(input())
    out.append(nums[num])


sys.stdout.write("\n".join(out))