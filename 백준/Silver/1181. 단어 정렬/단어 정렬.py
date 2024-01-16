N = int(input())
words = []

for _ in range(N):
    words.append(input())

# 중복 제거 위해 set 타입으로 변경
# -> set을 list 타입으로 변경 
words_list = set(words)
words = list(words_list)

# 오름차순 정렬
words.sort()
# 길이 순으로 정렬
words.sort(key = len)

for i in words:
    print(i)