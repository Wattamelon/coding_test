import sys

input = sys.stdin.readline


def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in zip(name, yearning):
        dict[i[0]] = i[1]
    for i in photo:
        res = 0
        for j in i:
            if j in dict:
                res += dict[j]
            else:
                pass

    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3]	[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]	[19, 15, 6]))