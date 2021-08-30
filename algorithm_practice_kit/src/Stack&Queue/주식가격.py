# https://programmers.co.kr/learn/courses/30/lessons/42584
# 나 이후로 나보다 크거나 같은 숫자의 갯수 구하기


def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        ans = 0
        target = prices[i]
        for j in range(i+1, len(prices)):
            compare = prices[j]
            if target <= compare:
                ans += 1
            else:
                ans += 1
                break
        answer.append(ans)
    answer.append(0)

    return answer


print(solution([1, 2, 3, 2, 3]))  # Expect [4, 3, 1, 1, 0]
print(solution([4, 2, 5, 1, 4]))  # Expect [1, 2, 1, 1, 0]
print(solution([1, 2, 3, 2, 3, 1]))  # Expect [5, 4, 1, 2, 1, 0]
