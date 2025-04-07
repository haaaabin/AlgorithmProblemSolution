from collections import Counter

N,C = map(int,input().split())

numbers = list(map(int,input().split()))
counter = Counter(numbers)
sorted_numbers = sorted(counter.items(), key=lambda x: (-x[1], numbers.index(x[0])))

result = []
for num, frq in sorted_numbers:
    result.extend([num] * frq)

print(*result)