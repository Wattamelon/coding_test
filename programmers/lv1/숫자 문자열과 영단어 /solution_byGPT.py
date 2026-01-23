# solution_byGPT.py (코테용 최적/안전한 풀이)
def solution(s: str) -> int:
    mp = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    out = []
    buf = []

    for ch in s:
        if "0" <= ch <= "9":
            out.append(ch)
        else:
            buf.append(ch)
            w = "".join(buf)
            if w in mp:
                out.append(mp[w])
                buf.clear()

    return int("".join(out))
