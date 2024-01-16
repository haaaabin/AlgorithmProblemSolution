import sys

N = int(sys.stdin.readline())
Nlist = []
for _ in range(N):
    Nlist.append(int(sys.stdin.readline()))
    
Nlist.sort()
Nlist_ = set(Nlist)
Nlist = list(Nlist_)

for i in Nlist:
    print(i)