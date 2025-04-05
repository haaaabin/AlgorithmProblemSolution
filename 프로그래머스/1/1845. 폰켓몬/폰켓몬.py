def solution(nums):
    temp = list(set(nums))
    
    if len(nums) // 2 < len(temp):
        return len(nums) // 2
    else:
        return len(temp)