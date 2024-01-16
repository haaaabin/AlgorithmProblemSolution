N = int(input())
Nlist = list(map(int,input().split()))

M = int(input())
Mlist = list(map(int,input().split()))

Nlist.sort()


def search(target,data):
    pl = 0
    pr = N -1
    
    while pl <= pr:
        pc = (pl + pr) //2
        if target == data[pc]:
            return True
        elif target > data[pc]:
            pl = pc + 1
        else:
            pr = pc - 1
        
    return False

for m in Mlist:
    if search(m,Nlist):
        print(1, end=" ")
    else:
        print(0, end =" ")