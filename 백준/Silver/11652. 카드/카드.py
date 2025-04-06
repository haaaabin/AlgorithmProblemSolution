import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
cards = [ int(input()) for _ in range(N)]
cards = Counter(cards)
counter_itmes = sorted(cards.items(), key=lambda x : (-x[1],x[0]))

print(counter_itmes[0][0])