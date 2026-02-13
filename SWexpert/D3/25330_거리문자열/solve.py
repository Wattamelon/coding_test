import sys


input = sys.stdin.readline


n = int(input())
out = []
for _ in range(n):
    n = list(map(int,input().strip()))
    nums_dict = {}
    for i in n:
        if i in nums_dict:
            nums_dict[i] += 1
        else:
            nums_dict[i] = 1
    error = False
    for i in nums_dict.values():
        if i != 2:
            error = True
            out.append("no")
            break
    if error == True:
        continue
    else:
        for i in range(len(n)):
            res = False
            if i + n[i] + 1 < len(n):
                if n[i + n[i] + 1] == n[i]:
                    res = True
                    continue
            if i - n[i] - 1 >= 0:
                if n[i - n[i] - 1] == n[i]:
                    res = True
            if res:
                out.append("yes")
            else:
                out.append("no")


sys.stdout.write("\n".join(out))



