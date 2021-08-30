# https://programmers.co.kr/learn/courses/30/lessons/42579
from heapq import heappush, heappop

def solution(genres, plays):
    answer = []
    d = dict()
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in d:
            d[genre] = [[], 0]
        d[genre][1] += play
        heappush(d[genre][0], (-play, i))
    sortedD = dict(sorted(d.items(), key=lambda item: -item[1][1]))
    for k, v in sortedD.items():
        added = 0
        while v[0] and added < 2:
            maxi = heappop(v[0])
            answer.append(maxi[1])
            added += 1
    return answer


print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
