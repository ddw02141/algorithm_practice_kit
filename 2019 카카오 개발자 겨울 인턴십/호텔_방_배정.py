from collections import defaultdict
from heapq import heappush, heappop, heapify


def solution(k, room_number):
    # 1 <= k <= 10^12
    answer = []
    answerDict = dict()
    rooms = list()
    roomToIdx = defaultdict(list)
    for idx, room in enumerate(room_number):
        if room not in rooms:
            heappush(rooms, room)
        heappush(roomToIdx[room], idx + 1)
    while rooms:
        room = heappop(rooms)
        indices = roomToIdx[room]
        if not indices:
            continue
        idx = heappop(indices)
        answerDict[idx] = room
        roomToIdx[room + 1] = roomToIdx[room + 1] + indices
        heapify(roomToIdx[room + 1])
        if room + 1 not in rooms:
            heappush(rooms, room + 1)
    # print(answerDict)
    for idx in range(len(room_number)):
        answer.append(answerDict[idx + 1])
    return answer


if __name__ == "__main__":
    print(solution(10, [1, 3, 4, 1, 3, 1]))  # Expect [1,3,4,2,5,6]
