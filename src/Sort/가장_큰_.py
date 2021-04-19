# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    # 9로 시작하는 숫자 -> 8로 시작하는 숫자 -> ... -> 1로 시작하는 숫자
    # 9, 99, 992, 98, 93 => 999, 999, 992, 988, 933
    # 93, 933
    # [3, 30, 34, 5, 9] => [9, 5, 34, 3, 30]
    # (마지막 숫자 붙인거, 원래 숫자길이, 원래 숫자)
    l = []
    for number in numbers:
        s = str(number)
        lenS = len(s)
        while len(s) < 4:
            s += s[-1]
        tup = (int(s), lenS, number)
        l.append(tup)
    l = sorted(l, key = lambda x: (-x[0], x[1]))
    answer = ''
    for ll in l:
        answer += str(ll[2])
    return answer