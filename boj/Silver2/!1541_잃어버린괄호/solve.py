import sys
input = sys.stdin.readline

x = input().strip()
nums = []
op = []
tmp = ""
for i in x:
    if i.isdigit() == True :
        tmp += i
    else:
        nums.append(tmp)
        tmp = ""
        op.append(i)

idx = 0

minus = False

while idx<len(nums):
