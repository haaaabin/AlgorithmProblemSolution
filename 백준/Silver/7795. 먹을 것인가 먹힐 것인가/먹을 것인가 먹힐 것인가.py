import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    
    count = 0
    j = 0
    
    for i in range(n):
        while j < m:
            if A[i] > B[j]:
                j +=1
            else:
                count +=j
                break
        else:
            count += m
    print(count)