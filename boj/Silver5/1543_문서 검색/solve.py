import sys
input = sys.stdin.readline

docs = input().strip()
word = input().strip()

idx_docs = 0
idx_word = 0
cnt = 0
while 1:
    if docs[idx_docs] == word[idx_word]:
        idx_docs += 1
        idx_word += 1
        if idx_word == len(word):
            cnt += 1
            idx_word = 0
    else:
        idx_docs = idx_docs - idx_word + 1
        idx_word = 0
    if idx_docs == len(docs):
        print(cnt)
        break;