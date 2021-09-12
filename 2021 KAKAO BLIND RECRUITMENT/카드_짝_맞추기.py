# https://programmers.co.kr/learn/courses/30/lessons/72415
# 카드번호: 0 ~ 6
# 0 ~ 6까지 카드가 모두 존재할 때 제거 순서로 가능한 경우의 수
# 7 * 6 * ... * 1 = 7! = 5040
# 7! * 2^7(두 카드 중 먼저 제거하는 카드를 고르는 경우의 수 = 2C1 = 2) = 5040 * 128 =  645,120
# 645,120 * 16(board 크기) = 10,321,920
from collections import defaultdict

BOARD_SIZE = 4
MAX_CARD = 7


def solution(board, r, c):
    answer = 0
    boardMap = defaultdict(list)
    visited = [False for _ in range(MAX_CARD)]
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y]:
                answer += 1  # 뒤집는 횟수
                boardMap[board[x][y]].append((x, y))
    print("answer:", answer)
    # print(boardMap)
    answer += backtrack(board, boardMap, visited, (r, c), 0, [])
    return answer


def backtrack(board, boardMap, visited, grid, moves, order):
    # print("backtrack", boardMap, visited, grid, moves)
    if len(boardMap) == sum(visited):
        return moves
    answer = float("inf")
    for i in range(1, MAX_CARD):
        if not visited[i] and i in boardMap:
            firstCard = boardMap[i][0]
            secondCard = boardMap[i][1]
            gridToFirstCard = move(board, visited, grid, firstCard)
            gridToSecondCard = move(board, visited, grid, secondCard)
            firstCardToSecondCard = move(board, visited, firstCard, secondCard)
            secondCardToFirstCard = move(board, visited, secondCard, firstCard)
            moves = moves + gridToFirstCard + firstCardToSecondCard
            visited[i] = True
            firstCardFirst = backtrack(board, boardMap, visited, secondCard, moves, order + [(i, 1)])
            if firstCardFirst < answer:
                answer = firstCardFirst
            moves = moves - gridToFirstCard - firstCardToSecondCard + gridToSecondCard + secondCardToFirstCard
            secondCardFirst = backtrack(board, boardMap, visited, firstCard, moves, order + [(i, 2)])
            if secondCardFirst < answer:
                answer = secondCardFirst
            moves = moves - gridToSecondCard - secondCardToFirstCard
            visited[i] = False
    return answer


# 0 1 0 1
# 좌 -> 우: 1
# 우 -> 좌: 2
def move(board, visited, grid1, grid2):
    xFirst = 0
    yFirst = 0
    x1, y1 = grid1
    x2, y2 = grid2
    # (x1, y1) -> (x2, y1)
    xFirst += moveX(board, visited, x1, x2, y1)
    # print("xFirst:", xFirst)
    # (x2, y1) -> (x2, y2)
    xFirst += moveY(board, visited, y1, y2, x2)
    # print("xFirst:", xFirst)
    # (x1, y1) -> (x1, y2)
    yFirst += moveY(board, visited, y1, y2, x1)
    # print("yFirst:", yFirst)
    # (x1, y2) -> (x2, y2)
    yFirst += moveX(board, visited, x1, x2, y2)
    # print("yFirst:", yFirst)

    # for i in range(BOARD_SIZE):
    #     for j in range(BOARD_SIZE):
    #         if not visited[board[i][j]]:
    #             print(board[i][j], " ", end='')
    #         else:
    #             print("0 ", end='')
    #     print()
    # print(grid1, "->", grid2)
    # print("min(", xFirst, ",", yFirst, "):", min(xFirst, yFirst))
    return min(xFirst, yFirst)


def moveX(board, visited, x1, x2, y):
    answer = 0
    if x1 != x2:
        if x2 > x1:
            if x2 == BOARD_SIZE - 1:
                answer += 1
                for x in range(x1+1, x2):
                    if board[x][y] and not visited[board[x][y]]:
                        answer += 1
            else:
                answer += (x2 - x1)
        else:  # x1 > x2
            if x2 == 0:
                answer += 1
                for x in range(x2+1, x1):
                    if board[x][y] and not visited[board[x][y]]:
                        answer += 1
            else:
                answer += (x1 - x2)
    return answer


def moveY(board, visited, y1, y2, x):
    answer = 0
    if y1 != y2:
        if y2 > y1:
            if y2 == BOARD_SIZE - 1:
                answer += 1
                for y in range(y1+1, y2):
                    if board[x][y] and not visited[board[x][y]]:
                        answer += 1
            else:
                answer += (y2 - y1)
        else:  # y1 > y2
            if y2 == 0:
                answer += 1
                for y in range(y2+1, y1):
                    if board[x][y] and not visited[board[x][y]]:
                        answer += 1
            else:
                answer += (y1 - y2)
    return answer


if __name__ == "__main__":
    # print("------------------ Test Case 1 ------------------")
    # sol = solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
    # ans = 14
    # assert ans == sol, f"Expected {ans} Actual {sol}"
    # print("------------------ Test Case 2 ------------------")
    # sol = solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1)
    # ans = 16
    # assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 3 ------------------")
    sol = solution([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0)
    ans = 32
    assert ans == sol, f"Expected {ans} Actual {sol}"
    [1, (1, 2), 5, (2, 1), 2, (1, 2), 6, (2, 1), 4, (1, 2), 3, (2, 1)]
    move([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], [False for _ in range(MAX_CARD)], (2, 2), (0, 0))
