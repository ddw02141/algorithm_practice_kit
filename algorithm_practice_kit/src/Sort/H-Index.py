def solution(citations):
    for hIndex in range(10000, 0, -1):
        over = 0
        for citation in citations:
            over += int(citation >= hIndex)
        if over >= hIndex:
            return hIndex
    return 0