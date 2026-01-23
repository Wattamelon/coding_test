# 다른 로직 풀이: replace로 통째로 치환 (짧고 직관적)
def solution_alt(s: str) -> int:
    mp = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    for w, d in mp.items():
        s = s.replace(w, d)
    return int(s)
