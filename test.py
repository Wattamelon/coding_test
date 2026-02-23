from collections import deque

def solution(food_times, k):
    food_times_idx = []
    for idx , nums in enumerate(food_times):
        tmp = {}
        tmp[idx+1] = nums
        food_times_idx.append(tmp) #[{1:3},{2:1}] ....
    queue = deque(food_times_idx)
    print(queue)
    while k:
        while queue[0].values() == [0]:
            queue.rotate(-1)
        tmp = list[queue[0].keys()][0]
        queue[0][tmp] -= 1
        "list(queue[0].values())[0] -= 1"
        queue.rotate(-1)
        k -= 1
    print(queue)
    print(queue[0])


solution([3, 1, 2],	5)