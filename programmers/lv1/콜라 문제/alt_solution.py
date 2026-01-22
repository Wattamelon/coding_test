# alt_solution.py (다른 로직: 수식으로 한 방에)
def solution(a, b, n):
    # 교환 1번 할 때마다 빈병 수는 (a-b)만큼 "순감소"함 (a 내고 b 받으니까)
    # 교환이 계속되려면 최소 b개는 남아야 마지막 교환까지 성립하는 형태가 됨
    return ((n - b) // (a - b)) * b
