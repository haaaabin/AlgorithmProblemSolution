import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    applicants = [tuple(map(int, input().split())) for _ in range(N)]
    
    # 서류 심사 성적을 기준으로 정렬
    applicants.sort(key=lambda x: x[0])

    # 면접 성적 비교
    max_rank = applicants[0][1]
    count = 1
    for i in range(1, N):
        if applicants[i][1] < max_rank:
            count += 1
            max_rank = applicants[i][1]

    print(count)