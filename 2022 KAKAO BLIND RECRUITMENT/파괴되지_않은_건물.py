def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    attacks = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for typ, r1, c1, r2, c2, amount in skill:
        flag = -1 if typ == 1 else 1
        attacks[r1][c1] += amount * flag
        attacks[r1][c2 + 1] -= amount * flag
        attacks[r2 + 1][c1] -= amount * flag
        attacks[r2 + 1][c2 + 1] += amount * flag

    for i in range(1, n):
        attacks[i][0] += attacks[i - 1][0]
    for j in range(1, m):
        attacks[0][j] += attacks[0][j - 1]
    for i in range(1, n):
        for j in range(1, m):
            attacks[i][j] = attacks[i][j] + attacks[i - 1][j] + attacks[i][j - 1] - attacks[i - 1][j - 1]
    for i in range(n):
        for j in range(m):
            if board[i][j] + attacks[i][j] > 0:
                answer += 1
    return answer


if __name__ == "__main__":
    print("---- Test case 1 ----")
    actual = solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
                      [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])
    expected = 10
    assert actual == expected, f"Expected {expected} but actual {actual}"

    print("---- Test case 2 ----")
    actual = solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]])
    expected = 6
    assert actual == expected, f"Expected {expected} but actual {actual}"
