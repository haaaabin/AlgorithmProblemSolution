N = int(input())
array1 = list(map(int,input().split()))
M = int(input())
array2 = list(map(int,input().split()))

array1.sort()

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) //2

        if target == data[mid]:
            return True
        elif target > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return False

for i in array2:
    print(1, end=" ") if binary_search(i,array1) else print(0, end=" ")