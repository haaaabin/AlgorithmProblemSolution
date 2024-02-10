import sys
input = sys.stdin.readline

nans =[]
for _ in range(9):
    n = int(input())
    nans.append(n)

for i in range(len(nans)):
    for j in range(1, len(nans)):
        if sum(nans) - (nans[i] + nans[j]) ==100:
            temp1 = nans[i]
            temp2 = nans[j]
            
nans.remove(temp1)
nans.remove(temp2)

for i in nans:
    print(i)