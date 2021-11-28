# https://programmers.co.kr/learn/courses/30/lessons/12979
import math


def solution(n, stations, w):
    answer = 0
    prev_isolated = 1
    for station in stations:
        isolated = max(0, station - w - 1)
        if isolated >= prev_isolated:
            answer = answer + math.ceil((isolated - prev_isolated + 1) / (2 * w + 1))
        prev_isolated = station + w + 1
    if n >= prev_isolated:
        answer = answer + math.ceil((n - prev_isolated + 1) / (2 * w + 1))
    return answer


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(11, [4, 11], 1)
    ans = 3
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(16, [9], 2)
    ans = 3
    assert ans == sol, f"Expected {ans} Actual {sol}"
