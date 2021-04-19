# https://programmers.co.kr/learn/courses/30/lessons/42628
import heapq

def solution(operations):
    minheap = []
    maxheap = []
    m = dict()
    for operation in operations:
        c, num = operation.split(" ")
        num = int(num)
        if c=="I":
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
            if num not in m:
                m[num] = 0
            m[num] += 1
        elif c=="D":
            if num == 1:
                while maxheap:
                    maxi = heapq.heappop(maxheap)
                    if -maxi in m and m[-maxi] > 0:
                        m[-maxi] -= 1
                        break
            elif num == -1:
                while minheap:
                    mini = heapq.heappop(minheap)
                    if mini in m and m[mini] > 0:
                        m[mini] -= 1
                        break
    # print(maxheap)
    # print(minheap)
    # print(m)
    finalMaxi = 0
    finalMini = 0
    while maxheap:
        maxi = heapq.heappop(maxheap)
        if -maxi in m and m[-maxi] > 0:
            finalMaxi = -maxi
            break
    while minheap:
        mini = heapq.heappop(minheap)
        if mini in m and m[mini] > 0:
            finalMini = mini
            break
    return [finalMaxi, finalMini]