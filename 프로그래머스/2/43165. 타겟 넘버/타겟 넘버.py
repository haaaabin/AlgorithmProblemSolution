def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        nonlocal answer
        # 모든 숫자를 처리했을 때
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return

        # 현재 숫자를 더하거나 빼는 두 가지 경우를 탐색
        dfs(index + 1, current_sum + numbers[index])  # 더하기
        dfs(index + 1, current_sum - numbers[index])  # 빼기

    # 탐색 시작
    dfs(0, 0)
    return answer