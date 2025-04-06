import sys
input = sys.stdin.readline

def sum_digitNum(serialNum):
    return sum(int(num) for num in serialNum if num.isdigit())

N = int(input())

serialNums = [input().rstrip() for _ in range(N)]
serialNums.sort(key = lambda x: (len(x), sum_digitNum(x),x))

for num in serialNums:
    print(num)