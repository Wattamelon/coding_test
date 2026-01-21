# solution_byGPT.py
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name_to_idx = {}
idx_to_name = [""] * (n + 1)  # 1-index

for i in range(1, n + 1):
    name = input().strip()
    idx_to_name[i] = name
    name_to_idx[name] = i

out = []
for _ in range(m):
    q = input().strip()
    if q.isdigit():
        out.append(idx_to_name[int(q)])
    else:
        out.append(str(name_to_idx[q]))

sys.stdout.write("\n".join(out))
