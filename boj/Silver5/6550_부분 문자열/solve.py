import sys
input = sys.stdin.readline


while 1:
    try:
        s , t = input().split()
        idx_s = 0
        idx_t = 0
        tmp = []
        s = list(s)
        while idx_t < len(t) and idx_s < len(s):
            if s[idx_s] == t[idx_t]:
                tmp.append(s[idx_s])
                idx_s += 1
                idx_t += 1
            else:
                idx_t += 1
        if s == tmp :
            print("Yes")
        else:
            print("No")
    except:
        break

"""while 1:
    try:
        s , t = map(str, input().split())
        first = list(s)
        for i in t :
            if first and i == first[0]:
                first.pop(0)
        if not first :
            print("Yes")
        else:
            print("No")
    except:
        break
"""