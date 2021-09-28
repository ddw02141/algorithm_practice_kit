# https://programmers.co.kr/learn/courses/30/lessons/72416
# https://yabmoons.tistory.com/625


def solution(sales, links):
    sales.insert(0, -1)
    tree = [[] for _ in range(len(sales))]
    for parent, child in links:
        tree[parent].append(child)
    dp = [[float("inf"), float("inf")] for _ in range(len(sales))]
    # dp[i][0] = i가 워크숍에 참석하지 않을 때, i를 루트로 가지는 직원들이 워크숍에 참석 할 때 직원 매출의 최소값
    # dp[i][1] = i가 워크숍에 참석할 때, i를 루트로 가지는 직원들이 워크숍에 참석 할 때 직원 매출의 최소값
    dfs(1, tree, sales, dp)
    # print(dp)
    return min(dp[1][0], dp[1][1])


def dfs(node, tree, sales, dp):
    childs = tree[node]
    if not childs:
        # Leaf Node
        dp[node][0] = 0
        dp[node][1] = sales[node]
        return
    for child in childs:
        dfs(child, tree, sales, dp)
    summ = sum(min(dp[child][0], dp[child][1]) for child in childs)
    dp[node][1] = sales[node] + summ
    net = float("inf")
    attendee = -1
    for child in childs:
        if dp[child][1] - dp[child][0] < net:
            net = dp[child][1] - dp[child][0]
            attendee = child
    # print("node", node, "attendee", attendee)
    dp[node][0] = summ - min(dp[attendee][0], dp[attendee][1]) + dp[attendee][1]


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
                   [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])
    ans = 44
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]])
    ans = 6
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 3 ------------------")
    sol = solution([5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]])
    ans = 5
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 4 ------------------")
    sol = solution([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]])
    ans = 2
    assert ans == sol, f"Expected {ans} Actual {sol}"
