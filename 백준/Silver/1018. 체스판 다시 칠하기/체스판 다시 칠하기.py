import sys
input = sys.stdin.readline

N, M = map(int, input().split())

chess=[]
result=[]

for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        paint_w = 0
        paint_b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if chess[x][y] != 'W':
                        paint_w +=1
                    else:
                        paint_b +=1
                else:
                    if chess[x][y] != 'B':
                        paint_w += 1
                    else:
                        paint_b += 1
        result.append(paint_w)
        result.append(paint_b)
        
print(min(result))