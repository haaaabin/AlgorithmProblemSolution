import math

def prime(a):
    if a == 1:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True
            
T = int(input())

for _ in range(T):
    n = int(input())
    A = n //2
    B = n //2
    for i in range(n//2):
        if prime(A) and prime(B):
            print(A,B)
            break
        else:
            A -=1
            B +=1