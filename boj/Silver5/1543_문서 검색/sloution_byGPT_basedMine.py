import sys
input = sys.stdin.readline

docs = input().rstrip()
word = input().rstrip()

idx_docs = 0
idx_word = 0
cnt = 0

while idx_docs < len(docs):
    if docs[idx_docs] == word[idx_word]:
        idx_docs += 1
        idx_word += 1
        if idx_word == len(word):
            cnt += 1
            idx_word = 0
    else:
        idx_docs = idx_docs - idx_word + 1
        idx_word = 0

print(cnt)
