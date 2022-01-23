import math


def solution(a, b, g, s, w, t):
    n = len(g)

    minAnswer = 2 ** 31 - 1
    if a == sum(g):
        maxAnswer = 0
        for i, gg in enumerate(g):
            if gg > 0:
                maxAnswer = max(maxAnswer, math.ceil(gg / (w[i] * t[i])) * 2 - 1)
        minAnswer = min(minAnswer, maxAnswer)
    if b == sum(s):
        maxAnswer = 0
        for i, ss in enumerate(s):
            if ss > 0:
                maxAnswer = max(maxAnswer, math.ceil(ss / (w[i] * t[i])) * 2 - 1)
        minAnswer = min(minAnswer, maxAnswer)
    if a != sum(g) and b != sum(s):
        minAnswer = 0

    left = 1
    right = answer = 2 ** 31 - 1
    while left < right:
        mid = left + (right - left) // 2
        mineral = getMineral(g, s, w, t, n, mid)
        if mineral >= a + b:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    return max(minAnswer, answer)


def getMineral(g, s, w, t, n, time):
    mineral = 0
    for i in range(n):
        if time < t[i]:
            continue
        count = 1 + (time - t[i]) // (2 * t[i])
        mineral += min(g[i] + s[i], w[i] * count)
    return mineral


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1])
    ans = 499
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(10, 10, [100], [100], [7], [10])
    ans = 50
    assert ans == sol, f"Expected {ans} Actual {sol}"
