# https://programmers.co.kr/learn/courses/30/lessons/87377?language=python3

def solution(line):
    intersects = set()
    for i, l1 in enumerate(line):
        for l2 in line[i + 1:]:
            a1, b1, c1 = l1
            a2, b2, c2 = l2
            denom = a1 * b2 - a2 * b1
            if denom == 0:
                continue
            x = (b1 * c2 - c1 * b2) / denom
            y = (c1 * a2 - a1 * c2) / denom
            if x == int(x) and y == int(y):
                intersects.add((int(x), int(y)))
    min_x = min(intersect[0] for intersect in intersects)
    max_x = max(intersect[0] for intersect in intersects)
    min_y = min(intersect[1] for intersect in intersects)
    max_y = max(intersect[1] for intersect in intersects)
    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1
    answer = ["." * len_x for _ in range(len_y)]
    for intersect in intersects:
        x, y = intersect
        newX, newY = x - min_x, y - min_y
        answer[newY] = answer[newY][:newX] + "*" + answer[newY][newX + 1:]
    return answer[::-1]


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
    ans = ["....*....",
           ".........",
           ".........",
           "*.......*",
           ".........",
           ".........",
           ".........",
           ".........",
           "*.......*"]
    assert ans == sol, f"Expected {ans} Actual {sol}"
