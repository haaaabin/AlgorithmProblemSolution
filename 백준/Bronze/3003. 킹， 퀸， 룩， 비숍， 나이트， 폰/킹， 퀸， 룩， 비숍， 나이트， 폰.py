chess = [1,1,2,2,2,8]
temp = list(map(int,input().split()))

for i in range(6):
    print(chess[i] - temp[i], end =" ")