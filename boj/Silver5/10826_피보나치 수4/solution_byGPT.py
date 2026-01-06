n = int(input())

a, b = 0, 1  # a=F(0), b=F(1)

for _ in range(n):
    a, b = b, a + b

print(a)

