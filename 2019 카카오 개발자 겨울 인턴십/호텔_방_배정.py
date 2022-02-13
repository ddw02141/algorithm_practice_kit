# https://programmers.co.kr/questions/21382
import sys

sys.setrecursionlimit(10000000)


def solution(k, room_number):
    # 1 <= k <= 10^12
    answer = []
    nextRoomToSeek = dict()
    for room in room_number:
        answer.append(findRoom(room, nextRoomToSeek))
    return answer


def findRoom(room, nextRoomToSeek):
    if room not in nextRoomToSeek:
        nextRoomToSeek[room] = room + 1
        return room

    finalRoom = findRoom(nextRoomToSeek[room], nextRoomToSeek)
    nextRoomToSeek[room] = finalRoom + 1
    return finalRoom


if __name__ == "__main__":
    print(solution(10, [1, 3, 4, 1, 3, 1]))  # Expect [1,3,4,2,5,6]
