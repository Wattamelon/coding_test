# solution_byGPT.py  (코테용 최적: min-heap)
import heapq

def solution(k, score):
    hall = []   # 명예의 전당(상위 k개)을 "최소힙"으로 관리 -> hall[0]이 최하위
    ans = []

    for s in score:
        if len(hall) < k:
            heapq.heappush(hall, s)
        else:
            if s > hall[0]:
                heapq.heapreplace(hall, s)  # pop+push 한 번에
        ans.append(hall[0])

    return ans
