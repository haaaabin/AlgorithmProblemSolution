temp = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(temp[i]):
            print(temp[i][j], end='')
    