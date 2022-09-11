# 단어 뒤집기
t = int(input())
answer = []


for _ in range(t):
    sentences = list(input().split())

    for words in sentences:
        print(words[::-1], end=' ')
