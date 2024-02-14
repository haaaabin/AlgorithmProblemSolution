def solution(a, b):
    answer = 0
    temp1 = int(str(a)+str(b))
    temp2 = 2 * a * b
    
    if temp1 >= temp2:
        answer = temp1
    else:
        answer = temp2
    return answer