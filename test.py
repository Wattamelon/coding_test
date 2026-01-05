from collections import defaultdict

group = defaultdict(list)
data = [("a", 10), ("b", 20), ("a", 30)]

for k, v in data:
    group[k].append(v)

print(group["a"])  # [10, 30]
print(group["b"])  # [20]
