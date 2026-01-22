def solution(a, b, n):
    answer = 0
    while n >= a:
        res = n%a
        n //= a
        n *= b
        answer += n
        n += res

    return answer