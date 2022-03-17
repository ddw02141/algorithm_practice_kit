from collections import deque, defaultdict

directedGraph = defaultdict(list)
N = 0


def solution(n, path, order):
    """

    @param n: 2 <= n <= 200,000
    @param path: len(path) == n - 1
    @param order: order[i][0] node should be visited before than visiting order[i][1] node
    @return: Returns whether all node visits are possible while keeping order conditions.
    """
    global N
    N = n
    graph = defaultdict(list)
    for start, end in path:
        graph[start].append(end)
        graph[end].append(start)
    global directedGraph

    visited = defaultdict(bool)
    q = deque([0])
    while q:
        node = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        for child in graph[node]:
            if not visited[child]:
                directedGraph[node].append(child)
                q.append(child)
    for start, end in order:
        directedGraph[start].append(end)
    return dfs(deque([0]))


def dfs(stack):
    discovered = defaultdict(int)
    finished = defaultdict(bool)
    nodeOrder = 1
    while stack:
        node = stack[-1]
        discovered[node] = nodeOrder
        nodeOrder += 1
        allChildDiscovered = True
        for child in directedGraph[node]:
            if discovered[child] == 0:
                stack.append(child)
                allChildDiscovered = False
            elif not finished[child]:
                return False
            elif discovered[node] < discovered[child]:
                continue
        if allChildDiscovered:
            finished[node] = True
            stack.pop()
    return True


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])
    ans = True
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]])
    ans = True
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 3 ------------------")
    sol = solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]])
    ans = False
    assert ans == sol, f"Expected {ans} Actual {sol}"
