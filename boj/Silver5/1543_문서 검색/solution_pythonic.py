import sys
input = sys.stdin.readline

docs = input().rstrip()
word = input().rstrip()

print(docs.count(word))
