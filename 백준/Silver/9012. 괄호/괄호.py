import sys
input =sys.stdin.readline

T = int(input())

for i in range(T):
    vps = input()
    stack = []
    
    for ps in vps:
        if ps == '(':
            stack.append(ps)
        elif ps == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    
    else:
        if not stack:
            print("YES")
        else:
            print("NO")