from math import ceil

def solution(progresses, speeds):
    answer = []
    
    days = [ceil((100-p) / s) for p,s in zip(progresses, speeds)]
    
    current = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = days[i]
            count = 1
    answer.append(count)
    
    return answer