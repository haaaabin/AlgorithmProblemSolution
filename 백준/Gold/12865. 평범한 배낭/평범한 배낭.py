import sys
input = sys.stdin.readline

n, k = map(int,input().split())

value = [[0] *(k+1) for j in range(n+1)]

bag = [[0,0]]

for i in range(1,n+1):
    bag.append(list(map(int,input().split())))
    
    

for i in range(n+1):
    for j in range(k+1):
        w = bag[i][0]
        v = bag[i][1]
        #넣을 수 있음?
        if w > j:
            value[i][j] = value[i-1][j]
        else:
            value[i][j] = max(value[i-1][j], value[i-1][j-w] +v)
        
print(value[n][k])