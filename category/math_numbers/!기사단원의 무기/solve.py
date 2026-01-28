def solution(number, limit, power):
    nums = [0]
    res = 0
    for i in range(1, number+1):
        cnt = 0
        for j in range(1,int(i**0.5)+1):
            if j*j == i:
                cnt += 1
                break
            elif i % j == 0:
                cnt += 2
        nums.append(cnt)
    for i in nums:
        if i > limit:
            res += power
        else:
            res += i
    return res

