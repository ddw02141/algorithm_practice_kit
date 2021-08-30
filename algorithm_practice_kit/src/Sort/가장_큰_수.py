# https://programmers.co.kr/learn/courses/30/lessons/42746
import collections
from functools import cmp_to_key


# 9 > 90 > 908
# 93 > 90
# 9 > 8
# 34 > 3 > 30
# 1 > 101 > 10
def solution(numbers):
    numbers.sort(key=cmp_to_key(lambda x,y: -int(str(x) + str(y)) + int(str(y) + str(x))))
    answer = ''
    for n in numbers:
        answer += str(n)
    if collections.Counter(answer)["0"] == len(answer):
        return "0"
    return answer


print(solution([3, 30, 34, 5, 9]))  # Expect "9534330"
print(solution([9, 99, 992, 98, 93, 933]))  # Expect "9999929893933"
print(solution([0, 0, 0, 0]))  # Expect "0"
print(solution([15, 151]))  # Expect "15151"
print(solution([90, 908, 89, 898, 10, 101, 1, 8, 9]))  # Expect "990908898988110110"
# [9, 90, 908, 89, 898, 8, 1, 101, 10]
# 101 vs 10 => 10110 vs 10101 => 10 vs 01
# 89 vs 898 => 89898 vs 89889 => 98 vs 89
# 90 vs 908 => 90908 vs 90890 => 908 vs 890
