def solution(participant, completion):
    d = dict()
    for c in completion:
        if c not in d:
            d[c] = 0
        d[c] += 1
    for p in participant:
        if p not in d:
            return p
        d[p] -= 1
        if d[p] == 0:
            d.pop(p, None)


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
