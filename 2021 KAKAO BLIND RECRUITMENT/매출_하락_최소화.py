def solution(sales, links):
    answer = 0
    return answer


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
