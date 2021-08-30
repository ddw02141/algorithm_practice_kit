def solution(priorities, location):
    q = []
    for i, priority in enumerate(priorities):
        q.append((priority, i))
    count = 1
    for target in range(9, 0, -1):
        lastIdx = -1
        for idx, (priority, i) in enumerate(q):
            if priority == target:
                if i == location:
                    return count
                else:
                    lastIdx = idx
                    count += 1
        if lastIdx > 0:
            q = q[lastIdx:] + q[:lastIdx]
        curQ = []
        for priority, i in q:
            if priority < target:
                curQ.append((priority, i))
        q = curQ


print(solution([2, 1, 3, 2], 0))  # Expect 3
print(solution([2, 1, 3, 2], 1))  # Expect 4
print(solution([2, 1, 3, 2], 2))  # Expect 1
print(solution([2, 1, 3, 2], 3))  # Expect 2
print(solution([1, 1, 9, 1, 1, 1], 0))  # Expect 5
print(solution([3, 3, 4, 2], 3))  # Expect 4
print(solution([1, 2, 3, 2], 1))  # Expect 3
