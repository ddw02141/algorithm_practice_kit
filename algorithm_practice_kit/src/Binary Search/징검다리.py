# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = 10 ** 9
    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        removed = 0
        prevDist = 0
        for i, rock in enumerate(rocks):
            if i == 0:
                if rock < mid:
                    removed += 1
                else:
                    prevDist = rock
            else:
                if rock - prevDist < mid:
                    removed += 1
                else:
                    prevDist = rock
        if distance - prevDist < mid:
            removed += 1
        # print("%d %d %d => removed %d" %(left, mid, right, removed))
        if removed <= n:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))  # Expect 4
print(solution(16, [4, 8, 111], 2))  # Expect 8
