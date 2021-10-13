def solution(board):
    n = len(board)
    dp = [[[[float("inf") for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    dfs((0, 0), (0, 1), n, board, dp, 0)
    answer = float("inf")
    for i in range(n):
        for j in range(n):
            answer = min(answer, dp[i][j][n - 1][n - 1])
    return answer


rowcol = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def dfs(grid1, grid2, n, board, dp, move):
    x1, y1 = grid1
    x2, y2 = grid2
    if dp[x1][y1][x2][y2] < move:
        return dp[x1][y1][x2][y2]
    dp[x1][y1][x2][y2] = move
    if grid1 == (n - 1, n - 1) or grid2 == (n - 1, n - 1):
        return move
    answer = float("inf")
    for r, c in rowcol:
        newX1, newX2 = x1 + r, x2 + r
        newY1, newY2 = y1 + c, y2 + c
        if 0 <= newX1 < n and 0 <= newX2 < n and 0 <= newY1 < n and 0 <= newY2 < n:
            if board[newX1][newY1] == 0 and board[newX2][newY2] == 0:
                if (newX1, newY1) < (newX2, newY2):
                    answer = min(answer, dfs((newX1, newY1), (newX2, newY2), n, board, dp, move + 1))
                else:
                    answer = min(answer, dfs((newX2, newY2), (newX1, newY1), n, board, dp, move + 1))
    if x1 == x2 and y1 + 1 == y2:
        #                grid2
        # grid1 grid2 => grid1
        if 0 <= x2 - 1 and board[x2 - 1][y2] == 0:
            newX2 = x1 - 1
            newY2 = y1
            if board[newX2][newY2] == 0:
                answer = min(answer, dfs((newX2, newY2), (x1, y1), n, board, dp, move + 1))
        # grid1 grid2 => grid1
        #                grid2
        if x2 + 1 < n and board[x2 + 1][y2] == 0:
            newX2 = x1 + 1
            newY2 = y1
            if board[newX2][newY2] == 0:
                answer = min(answer, dfs((x1, y1), (newX2, newY2), n, board, dp, move + 1))
        #                      grid1
        # grid1 grid2 =>       grid2
        if 0 <= x1 - 1 and board[x1 - 1][y1] == 0:
            newX1 = x2 - 1
            newY1 = y2
            if board[newX1][newY1] == 0:
                answer = min(answer, dfs((newX1, newY1), (x2, y2), n, board, dp, move + 1))
        # grid1 grid2 =>       grid2
        #                      grid1
        if x1 + 1 < n and board[x1 + 1][y1] == 0:
            newX1 = x2 + 1
            newY1 = y2
            if board[newX1][newY1] == 0:
                answer = min(answer, dfs((x2, y2), (newX1, newY1), n, board, dp, move + 1))
    if y1 == y2 and x1 + 1 == x2:
        # grid1 => grid2 grid1
        # grid2
        if 0 <= y2 - 1 and board[x2][y2 - 1] == 0:
            newX2 = x1
            newY2 = y1 - 1
            if board[newX2][newY2] == 0:
                answer = min(answer, dfs((newX2, newY2), (x1, y1), n, board, dp, move + 1))
        # grid1 => grid1 grid2
        # grid2
        if y2 + 1 < n and board[x2][y2 + 1] == 0:
            newX2 = x1
            newY2 = y1 + 1
            if board[newX2][newY2] == 0:
                answer = min(answer, dfs((x1, y1), (newX2, newY2), n, board, dp, move + 1))
        # grid1
        # grid2 => grid2 grid1
        if y1 + 1 < n and board[x1][y1 + 1] == 0:
            newX1 = x2
            newY1 = y2 + 1
            if board[newX1][newY1] == 0:
                answer = min(answer, dfs((x2, y2), (newX1, newY1), n, board, dp, move + 1))
        # grid1
        # grid2 => grid1 grid2
        if 0 <= y1 - 1 and board[x1][y1 - 1] == 0:
            newX1 = x2
            newY1 = y2 - 1
            if board[newX1][newY1] == 0:
                answer = min(answer, dfs((newX1, newY1), (x2, y2), n, board, dp, move + 1))
    return answer


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution([[0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 1, 1],
                    [1, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0]])
    ans = 7
    assert ans == sol, f"Expected {ans} Actual {sol}"
