# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    d = dict()
    for cloth in clothes:
        if cloth[1] not in d:
            d[cloth[1]] = []
        d[cloth[1]].append(cloth[0])

    answer = 1
    for k, v in d.items():
        answer *= (len(v) + 1)
    return answer - 1
