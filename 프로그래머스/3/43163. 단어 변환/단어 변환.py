from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    visited = set()
    q = deque()
    q.append((begin, 0))
    
    while q:
        current, count = q.popleft()
        
        if current == target:
            return count
        
        for word in words:
            if word not in visited and is_different(current, word):
                q.append((word, count + 1))
                visited.add(word)
                
    return 0

def is_different(word1, word2):
    diff = 0
    for a,b in zip(word1, word2):
        if a!= b:
            diff += 1
        if diff > 1:
            return False
    return diff == 1