import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    age, name = input().split()
    arr.append((int(age), name))

arr.sort(key=lambda x: x[0])  # 파이썬 sort는 안정 정렬이라 입력 순서 유지됨

sys.stdout.write("\n".join(f"{age} {name}" for age, name in arr))
