import sys

n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))
    
white = 0
blue = 0    
def cut(x,y,n):
    color = paper[x][y]
    global white, blue
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] !=color:
                cut(x,y,n//2)
                cut(x+n//2,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y+n//2,n//2)
                return 0
    
    if color == 0:
        white +=1
    else:
        blue +=1
        
cut(0,0,n)
print(white, blue, sep ="\n")