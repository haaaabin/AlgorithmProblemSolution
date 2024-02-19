from collections import Counter

def solution(array):
    answer = Counter(array)
    modes =[]
    max_count = max(answer.values())
    
    for k, v in answer.items():
        if v == max_count:
            modes.append(k)
        
    if len(modes) == 1:
        return modes[0]
    else:
        return -1