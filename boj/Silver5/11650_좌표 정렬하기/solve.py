import sys

input = sys.stdin.readline

n = int(input())

pos = [tuple(map(int,input().split())) for _ in range(n)]

pos.sort(key = lambda x : (x[0],x[1]))
sys.stdout.write("\n".join(f"{x} {y}" for x , y in pos))