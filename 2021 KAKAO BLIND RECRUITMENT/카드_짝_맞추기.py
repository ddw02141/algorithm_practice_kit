def solution(board, r, c):
    answer = 0
    return answer


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
    ans = 14
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1)
    ans = 16
    assert ans == sol, f"Expected {ans} Actual {sol}"
