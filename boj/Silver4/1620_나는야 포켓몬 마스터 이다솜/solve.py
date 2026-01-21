import sys
input = sys.stdin.readline

n , m = map(int,input().split())
poketmons_dict = {}
poketmons_list = []
for i in range(1,n+1):
    tmp = input().rstrip()
    poketmons_dict[tmp] = str(i)
    poketmons_list.append(tmp)

res = []
for _ in range(m):
    problem = input().rstrip()
    if problem.isdigit() is True:
        res.append(poketmons_list[int(problem)-1])
    else:
        res.append(poketmons_dict[problem])

sys.stdout.write("\n".join(res))
