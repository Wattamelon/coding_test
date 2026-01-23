def solution(data, ext, val_ext, sort_by):
    string = {"code" : 0  , "date":1,"maximum":2,"remain":3}
    extracted = []
    for i in data:
        if i[string[ext]] < val_ext:
            extracted.append(i)
    return sorted(extracted , key = lambda x : x[string[sort_by]])

"""
코드번호 제조일 최대수량 현재수량
"""