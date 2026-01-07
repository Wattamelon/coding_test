import sys
input = sys.stdin.readline

docs = input().rstrip()
word = input().rstrip()

i = 0
cnt = 0
L = len(word)

while i <= len(docs) - L:
    if docs[i:i+L] == word:
        cnt += 1
        i += L
    else:
        i += 1

print(cnt)
