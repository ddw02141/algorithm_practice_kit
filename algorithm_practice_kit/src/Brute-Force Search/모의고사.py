def solution(answers):
    ans = []
    score1 = 0
    score2 = 0
    score3 = 0
    stu1Pattern = [1, 2, 3, 4, 5]
    stu2Pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3Pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, answer in enumerate(answers):
        if stu1Pattern[i % len(stu1Pattern)] == answer:
            score1 += 1
        if stu2Pattern[i % len(stu2Pattern)] == answer:
            score2 += 1
        if stu3Pattern[i % len(stu3Pattern)] == answer:
            score3 += 1
    maxScore = max(score1, score2, score3)
    if score1 == maxScore:
        ans.append(1)
    if score2 == maxScore:
        ans.append(2)
    if score3 == maxScore:
        ans.append(3)
    return ans


print(solution([5, 5, 5, 1, 4, 1]))  # Expect [1,3]
print(solution([1, 2, 5, 5, 2]))  # Expect [1]
print(solution([3, 3, 1, 1, 1, 1, 2, 3, 4, 5]))  # Expect [1,3]
