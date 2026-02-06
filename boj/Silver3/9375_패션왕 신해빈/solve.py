import sys
input = sys.stdin.readline

test = int(input())
cnt = 1
for _ in range(test):
    x = int(input())
    clothese = {}
    for i in range(x):
        name,category = input().split()
        if category not in clothese:
            clothese[category] = [name]
        else:
            clothese[category] = clothese[category] + [name]
    if len(clothese) == 1:

        print(len(list(clothese.values())[0]))
        continue
    for i in clothese:
        cnt *= len(clothese[i])+1
    print(cnt-1)
