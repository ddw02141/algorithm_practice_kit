from heapq import heappush, heappop


def solution(n, start, end, roads, traps):
    fromList = [[] for _ in range(n + 1)]
    toList = [[] for _ in range(n + 1)]
    for p, q, s in roads:
        fromList[p].append((q, s))
        toList[q].append((p, s))
    distance = [[float("inf") for _ in range(2)] for _ in range(n + 1)]
    distance[start][0] = 0
    distance[start][1] = 0
    heap = [(0, start, False)]
    while heap:
        curDist, node, isReversed = heappop(heap)
        targetList = fromList
        if isReversed:
            targetList = toList
        for childNode, dist in targetList[node]:
            if childNode in traps:
                if distance[node][1 if isReversed else 0] + dist < distance[childNode][0 if isReversed else 1]:
                    distance[childNode][0 if isReversed else 1] = distance[node][1 if isReversed else 0] + dist
                    heappush(heap, (distance[childNode][0 if isReversed else 1], childNode, not isReversed))
            else:
                if distance[node][1 if isReversed else 0] + dist < distance[childNode][1 if isReversed else 0]:
                    distance[childNode][1 if isReversed else 0] = distance[node][1 if isReversed else 0] + dist
                    heappush(heap, (distance[childNode][1 if isReversed else 0], childNode, isReversed))
    return min(distance[end][0], distance[end][1])


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
    ans = 5
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
    ans = 4
    assert ans == sol, f"Expected {ans} Actual {sol}"
