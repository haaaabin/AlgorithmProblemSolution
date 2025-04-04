def solution(numbers):
    nums = [0,1,2,3,4,5,6,7,8,9]
    numbers.sort()
    result = 0
    for i in nums:
        if i not in numbers:
            result += i
    return result