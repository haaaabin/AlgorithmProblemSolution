import sys
input = sys.stdin.readline

m = []
for _ in range(10):
    m.append(int(input()))
    
scores = 0    
for i in m:
    scores += i
    if scores >=100:
        if abs(100-scores) > abs(100-(scores-i)):
            scores -=i
            break
print(scores) 