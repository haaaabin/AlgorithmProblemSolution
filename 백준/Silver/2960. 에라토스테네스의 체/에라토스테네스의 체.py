N, K = map(int,input().split())

nums = [ i for i in range(2, N+1)]
erase = []
while len(nums) > 0:
    p = nums[0]     #아직 지우지 않은 수 중 가장 작은 수
    temp = []
    for i in range(len(nums)):
        if nums[i] % p == 0:
            erase.append(nums[i])
        else:
            temp.append(nums[i])            
    nums = temp
    
print(erase[K-1])