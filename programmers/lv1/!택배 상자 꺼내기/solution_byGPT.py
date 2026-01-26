# solution_byGPT.py (가장 코테용: 간단/안전/직관)
def solution(n, w, num):
    total_rows = (n + w - 1) // w          # 총 층 수
    r = (num - 1) // w                      # num이 있는 층(0-based)
    p = (num - 1) % w                       # 그 층에서의 순번(0-based)

    # num이 실제로 놓인 "열(col)" 계산 (지그재그라서 홀수 층은 반대로)
    col = p if (r % 2 == 0) else (w - 1 - p)

    # 위로 몇 개가 더 있는지 세기 (층 수 최대 100이라 그냥 루프가 가장 안전)
    cnt = 1  # 자기 자신 포함
    last_len = n - (total_rows - 1) * w     # 마지막 층 상자 개수(1~w)

    for rr in range(r + 1, total_rows):
        if rr != total_rows - 1:
            cnt += 1                        # 마지막 층이 아니면 무조건 해당 열에 상자 존재
        else:
            # 마지막 층은 부분일 수 있어서 열에 존재하는지 체크
            if last_len == w:
                cnt += 1
            else:
                if (rr % 2 == 0):           # 마지막 층이 L->R 채움
                    if col < last_len:
                        cnt += 1
                else:                       # 마지막 층이 R->L 채움
                    if col >= w - last_len:
                        cnt += 1

    return cnt
