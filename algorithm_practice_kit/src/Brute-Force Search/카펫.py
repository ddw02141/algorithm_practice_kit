def solution(brown, yellow):
    sumi = 2 + brown // 2
    for x in range(1, sumi // 2 + 1):
        y = sumi - x
        if yellow + brown == x * y:
            return [y, x]
    return []


print(solution(10, 2))
print(solution(8, 1))
