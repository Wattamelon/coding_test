from collections import deque


def solution(k, score):
    nums = deque()
    answer = []
    for i in score:
        if len(nums) < k:
            nums.append(i)
            nums = deque(sorted(nums))
            answer.append(nums[0])
        else:
            if i > nums[0]:
                nums[0] = i
                nums = deque(sorted(nums))
                answer.append(nums[0])

    return answer



print(solution(3,[10, 100, 20, 150, 1, 100, 200]))