def solution(n, start, end, roads, traps):
    answer = 0
    map = [[] for _ in range(n + 1)]
    rMap = [[] for _ in range(n + 1)]
    for p, q, s in roads:
        map[p].append((q, s))
        if p in traps:
            rMap[q].append((p, s))
        if q in traps:
            rMap[q].append((p, s))
    isReversed = False
    visited = [False for _ in range(n+1)]
    Rvisited = [False for _ in range(n + 1)]
    print(map)
    print(rMap)
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
