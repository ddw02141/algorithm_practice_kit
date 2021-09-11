# https://programmers.co.kr/learn/courses/30/lessons/72413
# s -> x -> a
# s -> x -> b
# answer = (s -> x) + (x -> a) + (x -> b)


def solution(n, s, a, b, fares):
    answer = float("inf")
    road = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    for src, dest, wage in fares:
        road[src][dest] = wage
        road[dest][src] = wage
    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(start, n + 1):
                if start == end:
                    road[start][end] = 0
                    continue
                if mid == start or mid == end:
                    continue
                if road[start][end] > road[start][mid] + road[mid][end]:
                    road[start][end] = road[start][mid] + road[mid][end]
                if road[end][start] > road[mid][start] + road[end][mid]:
                    road[end][start] = road[mid][start] + road[end][mid]
    for x in range(1, n + 1):
        answer = min(answer, road[s][x] + road[x][a] + road[x][b])
    return answer


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(6, 4, 6, 2,
                   [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                    [1, 6, 25]])
    ans = 82
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
    ans = 14
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 3 ------------------")
    sol = solution(6, 5, 4, 6,
                   [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]])
    ans = 18
    assert ans == sol, f"Expected {ans} Actual {sol}"
