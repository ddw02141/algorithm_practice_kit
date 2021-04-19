# 7! = 5040
from itertools import permutations
import math


def solution(numbers):
    answer = 0
    nums = [num for num in numbers]
    s = set()
    for c in range(1, len(numbers) + 1):
        l = list(permutations(nums, c))
        for ll in l:
            target = int("".join(ll))
            s.add(target)

    for ss in s:
        answer += int(isPrime(ss))

    return answer


def isPrime(n):
    if n == 0:
        return False
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


print(solution("011"))
