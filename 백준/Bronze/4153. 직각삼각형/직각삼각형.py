import sys
input = sys.stdin.readline

while(True):
    temp = list(map(int,input().split()))
    
    if(temp[0] == 0 and temp[1] == 0 and temp[2] ==0):
        break
    
    temp.sort()
        
    if ((temp[2])**2) == ((temp[0])**2 + (temp[1]**2)):
        print("right")
    else:
        print("wrong")