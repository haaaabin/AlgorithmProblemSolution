def solution(numbers):
    answer = []
    
    for j in range(len(numbers)):
        for i in range(j+1 , len(numbers)):
            answer.append(numbers[j] + numbers[i])
    return sorted(list(set(answer)))