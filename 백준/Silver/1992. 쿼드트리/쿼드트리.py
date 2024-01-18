import sys

N = int(input())

video = []
for i in range(N):
    video.append(list(map(int,sys.stdin.readline().strip())))
    
def Quard_Tree(x,y,n):
    result = video[x][y]    #[0][0] 압축 결과 -> 1
    for i in range(x, x+n):
        for j in range(y, y+n):
            if video[i][j] != result:
                print("(",end ="")
                Quard_Tree(x, y, n//2)
                Quard_Tree(x, y+n//2, n//2)
                Quard_Tree(x+n//2, y, n//2)
                Quard_Tree(x+n//2, y+n//2, n//2)
                print(")",end ="")
                return 0
    print(result, end ="")
    
Quard_Tree(0,0,N)