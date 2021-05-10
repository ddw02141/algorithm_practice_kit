import math

def solution(progresses, speeds):
    answer = []
    idx = 0
    ans = 0
    while idx < len(progresses):
        progress = progresses[idx]
        speed = speeds[idx]
        if progress < 100:
            if ans > 0:
                answer.append(ans)
            time = math.ceil((100 - progress) / speed)
            for i in range(idx, len(progresses)):
                progresses[i] += (time * speeds[i])
            ans = 1
        else:
            ans += 1
        idx += 1
    if ans > 0:
        answer.append(ans)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))  # Expect [2,1]
print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]))  # Expect [1,3,2]
