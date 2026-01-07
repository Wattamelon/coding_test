import sys
input = sys.stdin.readline

n = int(input())
words = {input().strip() for _ in range(n)}  # set으로 중복 제거

words = sorted(words, key=lambda x: (len(x), x))

sys.stdout.write("\n".join(words))
