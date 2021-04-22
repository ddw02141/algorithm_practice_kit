# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 10 ** 18
    left = 0
    right = 10 ** 18
    while left <= right:
        mid = (left + right) // 2
        ans = 0
        for time in times:
            ans += (mid // time)
        if ans < n:
            left = mid + 1
        elif ans >= n:
            answer = min(answer, mid)
            right = mid - 1
    return answer


print(solution(0, [7, 10]))
print(solution(1, [2, 2]))
print(solution(6, [7, 10]))
print(solution(10 ** 9, [10 ** 9]))
