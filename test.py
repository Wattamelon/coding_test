n , k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[0] < b[0]:
        a[0] , b[0] = b[0] , a[0]
        idx = 0
        cnt = 1
        while a[idx] > a[cnt]:
            a[cnt] , a[idx] = a[idx] , a[cnt]
            idx += 1
            cnt += 1
        idx = 0
        cnt = 1
        while b[idx] < b[cnt]:
            b[cnt], b[idx] = b[idx], b[cnt]
            idx += 1
            cnt += 1

print(sum(a))

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""