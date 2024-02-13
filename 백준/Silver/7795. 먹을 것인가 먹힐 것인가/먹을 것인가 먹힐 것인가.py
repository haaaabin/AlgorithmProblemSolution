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
    start = 0
    
    for i in range(n):
        while True:
            if start == m or A[i]<=B[start]:
                count +=start
                break
            else:
                start += 1
    print(count)