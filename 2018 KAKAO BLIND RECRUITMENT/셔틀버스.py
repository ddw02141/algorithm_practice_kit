# https://programmers.co.kr/learn/courses/30/lessons/17678
# 마지막 셔틀을, 꼴찌로 타면 된다
# 마지막 셔틀이 올 때 남아있는 사람의 도착 시간 정보를 알기 위해서는, 이전 셔틀이 왔을 때 누구까지를 데려갔는지를 알아야 함!
# Brute Force로 셔틀 태워 보내고, 마지막 남은 사람들 리스트에서 lower bound 구하면 될듯?!
from bisect import bisect_right


def solution(n, t, m, timetable):
    timetable = [get_minutes(time) for time in timetable]
    timetable.sort()
    bus_arrival = get_minutes("09:00") - t
    for _ in range(n - 1):
        bus_arrival += t
        ub = bisect_right(timetable, bus_arrival)
        timetable = timetable[min(ub, m):]
    bus_arrival += t
    ub = bisect_right(timetable, bus_arrival)
    timetable = timetable[:ub]
    if not timetable or len(timetable) < m:
        answer = bus_arrival
    else:
        # 내가 제껴야 하는 사람 = timetable[m-1]
        # timetable[m-1] > bus_arrival => bus_arrival
        if timetable[m - 1] > bus_arrival:
            answer = bus_arrival
        else:
            answer = timetable[m - 1] - 1
    return get_time_str(answer)


def get_minutes(time_str):
    hh, mm = time_str.split(":")
    return int(hh) * 60 + int(mm)


def get_time_str(minutes):
    hh = minutes // 60
    mm = minutes - hh * 60
    return "{:02d}:{:02d}".format(hh, mm)


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
    ans = "09:00"
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(2, 10, 2, ["09:10", "09:09", "08:00"])
    ans = "09:09"
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 3 ------------------")
    sol = solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
    ans = "08:59"
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 4 ------------------")
    sol = solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])
    ans = "00:00"
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 5 ------------------")
    sol = solution(1, 1, 1, ["23:59"])
    ans = "09:00"
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 6 ------------------")
    sol = solution(10, 60, 45,
                   ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                    "23:59", "23:59", "23:59", "23:59", "23:59"])
    ans = "18:00"
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 7 ------------------")
    sol = solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01", "00:02", "00:03", "00:04"])
    ans = "00:00"
    assert ans == sol, f"Expected {ans} Actual {sol}"
