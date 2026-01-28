# solution_byGPT.py
def solution(n: int) -> int:
    # n을 3진법으로 만들면서(뒤에서부터) 그 자체가 "뒤집힌 3진수"가 되게 만든다.
    # 그 뒤집힌 3진수를 다시 10진수로 해석(3진수 누적)하면 답.
    res = 0
    while n > 0:
        n, r = divmod(n, 3)   # r: 현재 자리(3진법)
        res = res * 3 + r     # 뒤집힌 3진수를 3진수로 누적
    return res
