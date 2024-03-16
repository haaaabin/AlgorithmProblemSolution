import sys
input = sys.stdin.readline

M = int(input())
S = set()
for i in range(M):
    comment = input().split()
    if comment[0] == "add":
        if int(comment[1]) not in S:
            S.add(int(comment[1]))
    elif comment[0] == "remove":
        if int(comment[1]) in S:
            S.discard(int(comment[1]))
    elif comment[0] == "check":
        if int(comment[1]) in S:
            print(1)
        else:
            print(0)
    elif comment[0] == "toggle":
        if int(comment[1]) in S:
            S.discard(int(comment[1]))
        else:
            S.add(int(comment[1]))
    elif comment[0] == "all":
        S = set(range(1, 21))
    elif comment[0] == "empty":
        S.clear()