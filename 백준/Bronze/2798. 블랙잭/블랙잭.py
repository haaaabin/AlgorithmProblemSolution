import sys
input = sys.stdin.readline

N,M =map(int,input().split())
cards=list(map(int,input().split()))

sum =0
threecards = []

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = cards[i]+cards[j]+cards[k]
            if sum > M:
                continue
            else:
                threecards.append(sum)
                
print(max(threecards))   