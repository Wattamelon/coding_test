import sys
input = sys.stdin.readline

n, m = map(int, input().split())

heard = {input().strip() for _ in range(n)}
seen  = {input().strip() for _ in range(m)}

res = sorted(heard & seen)

sys.stdout.write(str(len(res)) + "\n" + "\n".join(res))
