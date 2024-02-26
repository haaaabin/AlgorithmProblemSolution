from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
card1 = list(map(int,input().split()))
M = int(input())
card2 = list(map(int, input().split()))

counter = Counter(card1)            #리스트에 있는 각 문자의 개수를 Count

for card in card2:
    print(counter[card], end =" ")