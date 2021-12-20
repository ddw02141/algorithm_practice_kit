# https://programmers.co.kr/learn/courses/30/lessons/42894
def solution(board):
    answer = 0
    n = len(board)

    while rectangle_exists(n, board):
        answer += 1

    return answer


def rectangle_exists(n, board):
    moves = [(0, 0, 1, 2), (0, 0, 2, 1), (0, -1, 2, 0), (0, -2, 1, 0), (0, -1, 1, 1), (0, -1, 2, 0)]
    targets = set()
    for i in range(n):
        for j in range(n):
            if board[i][j] and not board[i][j] in targets:
                targets.add(board[i][j])
                for x1, y1, x2, y2 in moves:
                    if can_make_rectangle(i + x1, j + y1, i + x2, j + y2, board[i][j], n, board):
                        for xx in range(i + x1, i + x2 + 1):
                            for yy in range(j + y1, j + y2 + 1):
                                board[xx][yy] = 0
                        return True
    return False


def can_make_rectangle(x1, y1, x2, y2, target, n, board):
    for z in [x1, y1, x2, y2]:
        if z < 0 or z >= n:
            return False
    num_target = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if board[x][y] == target:
                num_target += 1
            elif board[x][y] != 0:
                return False
            elif sum(board[xx][y] for xx in range(0, x)) != 0:
                return False
    return num_target == 4


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                    [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
                    [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
                    [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
                    [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]])
    ans = 2
    assert ans == sol, f"Expected {ans} Actual {sol}"
