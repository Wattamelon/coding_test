import sys
input = sys.stdin.readline

m , n = map(int,input().split())

out = []
prime_nums = []
if m == 1 or m == 2:
    m = 2
    out.append("2")
for i in range(m,n+1):
    prime = True
    if i % 2 == 0:
        continue
    else:
        half = int(i**0.5)+1
        for j in range(3,half,2):
            if i%j == 0:
                prime = False
                break
    if prime:
        out.append(str(i))


sys.stdout.write("\n".join(out))
