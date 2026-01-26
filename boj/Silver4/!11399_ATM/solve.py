n = int(input())

p = list(map(int,input().split()))
tmp = [0] * len(p)
p.sort()
tmp[0] = p[0]
for i in range(1,len(p)):
    tmp[i] = tmp[i-1] + p[i]

print(sum(tmp))