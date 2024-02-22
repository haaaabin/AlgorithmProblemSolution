def solution(age):
    answer = ''
    alpabet = "abcdefghij"
    for i in str(age):
        answer += alpabet[int(i)]
    return answer