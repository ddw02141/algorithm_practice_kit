# https://programmers.co.kr/learn/courses/30/lessons/42583
# 트럭 여러 대가 강을 가로지르는 "일차선" 다리를 "정해진" 순으로 건너려 합니다.
from collections import deque

def solution(bridgeLength, weight, truckWeights):
    bridge = deque()
    for _ in range(bridgeLength):
        bridge.append(0)
    trucks = deque(truckWeights)
    time = 0
    w = 0
    while bridge:
        time += 1
        popleft = bridge.popleft()
        w -= popleft
        if trucks:
            if w + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                w += truck
            else:
                bridge.append(0)
    return time


print(solution(2, 10, [7, 4, 5, 6]))  # Expect 8
print(solution(100, 100, [10]))  # Expect 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # Expect 110
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))  # Expect 19
