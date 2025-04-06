def solution(n):
    answer = list(sorted(str(n), reverse = True))
    answer = ''.join(answer)
    return int(answer)