n = int(input())

for i in range(n):
    temp = list(input())
    score = 0
    result = 0

    for text in temp:
        if text == 'O':
            score += 1
            result += score        
        else:
            score = 0
    print(result)