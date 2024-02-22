def solution(n, k):
    answer = 0
    if n < 10:
        answer = n * 12000 + k *2000
    elif n >= 10:
        s = k - (n //10)
        answer = n * 12000 + s * 2000        
    return answer