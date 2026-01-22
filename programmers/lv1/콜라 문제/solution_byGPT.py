# solution_byGPT.py (코테용 최적/가장 안전)
def solution(a, b, n):
    answer = 0
    while n >= a:
        q, r = divmod(n, a)      # q: 교환 횟수, r: 남는 병
        gained = q * b           # 이번 라운드에서 새로 받은 콜라 수
        answer += gained
        n = gained + r           # 새로 생긴 빈병 + 남은 빈병
    return answer
