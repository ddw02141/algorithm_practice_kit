# https://programmers.co.kr/learn/courses/30/lessons/81304
# https://tech.kakao.com/2021/07/08/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-for-tech-developers-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EC%84%A4/#:~:text=%ED%95%B4%EA%B2%B0%ED%95%A0%20%EC%88%98%20%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.-,%EB%AC%B8%EC%A0%9C%204,-%EB%AC%B8%EC%A0%9C%20%ED%92%80%EC%9D%B4%20%3A%20Lv4
from itertools import product
from heapq import heappush, heappop

INF = float("inf")


def solution(n, start, end, roads, traps):
    t = len(traps)
    roadMap = dict()
    visited = dict()
    distanceMap = dict()
    answer = INF
    # Cartesian product
    for trapStatus in product([0, 1], repeat=t):
        roadMap[trapStatus] = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
        visited[trapStatus] = [False for _ in range(n + 1)]
        distanceMap[trapStatus] = [INF for _ in range(n + 1)]
        for p, q, s in roads:
            pTrapped = qTrapped = False
            if p in traps and trapStatus[traps.index(p)]:
                pTrapped = True
            if q in traps and trapStatus[traps.index(q)]:
                qTrapped = True
            if pTrapped == qTrapped:
                roadMap[trapStatus][p][q] = min(roadMap[trapStatus][p][q], s)
            else:
                roadMap[trapStatus][q][p] = min(roadMap[trapStatus][q][p], s)
    initialTrapStatus = tuple(0 for _ in range(t))
    distanceMap[initialTrapStatus][start] = 0
    heap = [(0, start, initialTrapStatus)]
    while heap:
        curD, node, trapStatus = heappop(heap)
        visited[trapStatus][node] = True
        if node == end:
            answer = min(answer, curD)
            continue
        for childNode in range(n + 1):
            s = roadMap[trapStatus][node][childNode]
            if s != INF:
                trapStatus = tuple(ts for ts in trapStatus)
                nextTrapStatus = tuple(ts for ts in trapStatus)
                if childNode in traps:
                    nextTrapStatus = list(nextTrapStatus)
                    tIdx = traps.index(childNode)
                    nextTrapStatus[tIdx] = int(not trapStatus[tIdx])
                    nextTrapStatus = tuple(nextTrapStatus)
                if not visited[nextTrapStatus][childNode]:
                    if curD + s < distanceMap[nextTrapStatus][childNode]:
                        distanceMap[nextTrapStatus][childNode] = curD + s
                        heappush(heap, (distanceMap[nextTrapStatus][childNode], childNode, nextTrapStatus))
    return answer


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
    ans = 5
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
    ans = 4
    assert ans == sol, f"Expected {ans} Actual {sol}"
