import sys
input = sys.stdin.readline

def binary_search(target, data):
    start = 0
    end = len(target) -1

    while True:
        if start > end:
            return -1
        
        mid = (start + end) //2
        if target[mid] < data:
            start = mid + 1
        elif target[mid] > data:
            end = mid - 1
        else:
            return mid

T =int(input())

for i in range(T):
    N = int(input())
    note1 = list(map(int,input().split()))
    M = int(input())
    note2 = list(map(int,input().split()))
    note1.sort()
    
    for num in note2:
        if binary_search(note1, num) >= 0:
            print(1)
        else:
            print(0)