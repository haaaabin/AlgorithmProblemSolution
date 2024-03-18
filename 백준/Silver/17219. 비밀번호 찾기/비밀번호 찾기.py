import sys
input = sys.stdin.readline

N, M = map(int,input().split())

password = {}
for i in range(N):
    adr,pas = input().split()
    password[adr] = pas

for i in range(M):
    n = input().strip()
    print(password[n])  