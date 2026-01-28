# alt_solution.py (다른 로직: 문자열로 3진수 만들고 뒤집고 다시 변환)
def solution(n: int) -> int:
    digits = []
    while n > 0:
        n, r = divmod(n, 3)
        digits.append(str(r))      # 뒤에서부터 뽑히는 r을 그대로 append하면 이미 "뒤집힌" 상태의 문자열이 됨

    rev_base3 = "".join(digits)    # 뒤집힌 3진수 문자열
    return int(rev_base3, 3)       # 3진수로 해석해서 10진수로 변환
