def solution(age):
    answer = ''
    alpabet = ['a','b','c','d','e','f','g','h','i','j']
    for i in str(age):
        answer += alpabet[int(i)]
    return answer