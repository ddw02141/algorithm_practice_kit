# https://programmers.co.kr/learn/courses/30/lessons/42890
from collections import defaultdict
from itertools import combinations

DELIMITER = ":"


def solution(relation):
    answer = 0
    r = len(relation)
    c = len(relation[0])
    # 1 <= r <= 20
    # 1 <= c <= 8
    answerByNumColumns = defaultdict(list)
    for numColumn in range(1, c + 1):
        combis = list(combinations([i for i in range(c)], numColumn))
        combis = [set(combi) for combi in combis]
        # print(numColumn, ":", combis)
        for combi in combis:
            if isSuperset(combi, answerByNumColumns, numColumn):
                continue
            candidateKeys = []
            for row in relation:
                candidateKeys.append(":".join([row[i] for i in combi]))
            if len(set(candidateKeys)) == r:
                answerByNumColumns[numColumn].append(combi)
    for numColumn in range(1, c + 1):
        answer += len(answerByNumColumns[numColumn])
    return answer


def isSuperset(combi, answerByNumColumns, numColumn):
    for i in range(1, numColumn):
        existingCandidateKeys = answerByNumColumns[i]
        for existingCandidateKey in existingCandidateKeys:
            if existingCandidateKey.issubset(combi):
                return True
    return False


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution([["100", "ryan", "music", "2"],
                    ["200", "apeach", "math", "2"],
                    ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"],
                    ["500", "muzi", "music", "3"],
                    ["600", "apeach", "music", "2"]])
    ans = 2
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution([['a', 'aa'],
                    ['aa', 'a'],
                    ['a', 'a']])
    ans = 1
    assert ans == sol, f"Expected {ans} Actual {sol}"
