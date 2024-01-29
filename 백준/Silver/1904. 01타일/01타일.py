import sys
input = sys.stdin.readline

n = int(input())

tiles = [0] * 1000001

tiles[1] = 1
tiles[2] = 2

for i in range(3,n+1):
    tiles[i] = (tiles[i-2] + tiles[i-1]) % 15746

print(tiles[n])