N = int(input())

words = [input() for _ in range(N)]
temp = set(words)
words = list(temp)
words.sort(key=lambda x : (len(x) , x))

for word in words:
    print(word)