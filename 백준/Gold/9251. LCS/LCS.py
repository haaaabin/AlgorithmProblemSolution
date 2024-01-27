import sys
input = sys.stdin.readline

string_A = [0]+list(input().rstrip())
string_B = [0]+list(input().rstrip())

lcs = [[0] * (len(string_B)) for _ in range(len(string_A))]

for i in range(1,len(string_A)):
    for j in range(1,len(string_B)):
        if string_A[i] == string_B[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            
print(lcs[-1][-1])