import sys
input = sys.stdin.readline

string_A = [""]+list(input().rstrip())
string_B = [""]+list(input().rstrip())

lcs = [[""] * (len(string_B)) for _ in range(len(string_A))]


for i in range(1,len(string_A)):
    for j in range(1,len(string_B)):
        if string_A[i] == string_B[j]:
            lcs[i][j] = lcs[i-1][j-1] + string_A[i]
        else:
            if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]

result = lcs[-1][-1]
print(len(result), result , sep ="\n")