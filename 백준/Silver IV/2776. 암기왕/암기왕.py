import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    note1  = set(map(int,input().split()))
    m = int(input())
    note2 = map(int,input().split())
    
    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)