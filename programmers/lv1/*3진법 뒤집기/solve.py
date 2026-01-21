from collections import deque
def solution(n):
    rev_base = ''
    q = 3
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    rev_base = deque(rev_base)
    tmp = []
    while rev_base:
        tmp.append(rev_base.popleft())
    string = ""

    for i in tmp:
        string += i
    tmp = int(string,3)
    return tmp
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


print(solution(125))