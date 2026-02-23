from pandas.io.sas.sas_constants import dataset_length

n = int(input())
data = list(map(int,input().split()))

data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)