from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length) # 다리 위 상태
    truck_weights = deque(truck_weights) # 대기중인 트럭
    current_weight = 0 #현재 다리 위 총 무게
    
    while bridge:
        answer += 1
        # 1. 다리 맨 앞에서 나가는 트럭
        out = bridge.popleft()
        current_weight -= out
        
        # 2. 새로운 트럭을 넣을 수 있는지 확인
        if truck_weights:
            if current_weight + truck_weights[0] <=weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
            
    
    return answer