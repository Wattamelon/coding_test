fibs = [0,1]

n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for _ in range(n-1):
        fibs.append(fibs[-2]+fibs[-1])
    print(fibs[-1])