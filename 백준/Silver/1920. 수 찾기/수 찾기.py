N = int(input())
A = list(map(int,input().split()))

M = int(input())
B = list(map(int,input().split()))

A.sort()    # 1 2 3 4 5

def search(target,data):
    pl = 0
    pr = N-1
    
    while pl <= pr:
        pc = (pl+pr)//2
        if target == data[pc]:
            return True
        elif target > data[pc]:
            pl = pc+1
        else:
            pr = pc-1
    return False

for i in B:
    if search(i,A):
        print("1")
    else:
        print("0")