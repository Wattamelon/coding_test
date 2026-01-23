# solution_byGPT.py (가독성/성능 밸런스, 파이써닉)
def solution(data, ext, val_ext, sort_by):
    idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    e, s = idx[ext], idx[sort_by]

    # 리스트 컴프리헨션으로 필터 + 정렬
    return sorted([row for row in data if row[e] < val_ext], key=lambda row: row[s])
