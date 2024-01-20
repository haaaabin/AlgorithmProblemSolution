import sys
sys.setrecursionlimit(10**9)

tree = []

#for문 안 쓰는 이유 -> 입력 갯수가 정해져 있지 않음 
#빈칸이 들어오면 터져서 except로 감 -> break
while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break
    
def postorder(start,end):
    if start > end:
        return
    
    mid = start +1
    
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            mid = i
            break
    
    postorder(start+1, mid -1)      #왼쪽 트리 
    postorder(mid, end)             #오른쪽 트리
    print(tree[start])              #루트 노드
    
postorder(0, len(tree)-1)