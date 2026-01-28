def solution(number, limit, power):
    # 1. 각 번호의 약수 개수를 저장할 리스트 (0으로 초기화)
    # American: Initialize an array to store divisor counts
    divisors = [0] * (number + 1)

    # 2. 에라토스테네스의 체 원리 활용 (O(N log N))
    # 1부터 number까지 각 i의 배수들에 +1씩 더함
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1

    # 3. 제한 수치를 확인하며 철의 무게 합산
    total_iron = 0
    for count in divisors[1:]:  # 0번 인덱스 제외
        if count > limit:
            total_iron += power
        else:
            total_iron += count

    return total_iron

