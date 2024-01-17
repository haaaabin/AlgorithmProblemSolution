N = int(input())

#퀸이 놓을 수 있는 체스판 
Q_row = [0] * N
count = 0

def is_promising(x):
    for i in range(x):
        if Q_row[x] == Q_row[i] or abs(Q_row[x]- Q_row[i]) == abs(x-i):
            return False
    return True

def n_queens(x):
    global count
    if x == N:
        count += 1
        return
    else:
        #i는 열, x는 행
        for i in range(N):
            Q_row[x] = i
            if is_promising(x):
                n_queens(x+1)    
                
n_queens(0)
print(count)