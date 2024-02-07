import sys
input = sys.stdin.readline

h,m = map(int,input().split())
    
if(m >= 45) :
    miniute = m-45
    print(h, miniute)
else:
    if(h == 0):
        h = 24 
    miniute = (m+60) - 45
    h -= 1
    print(h,miniute)