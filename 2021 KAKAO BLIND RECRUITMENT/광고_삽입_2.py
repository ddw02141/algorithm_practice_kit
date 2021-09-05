# https://programmers.co.kr/learn/courses/30/lessons/72414?language=python3
# Segment Tree https://www.acmicpc.net/blog/view/9


def solution(play_time, adv_time, logs):
    play_time_seconds = get_seconds(play_time)
    adv_time_seconds = get_seconds(adv_time)
    time_limit = play_time_seconds + 1
    watchers = [0 for _ in range(time_limit)]
    for log in logs:
        start, end = log.split("-")
        start_seconds = get_seconds(start)
        end_seconds = get_seconds(end)
        watchers[start_seconds] += 1
        watchers[end_seconds] -= 1
    for i in range(1, time_limit):
        watchers[i] += watchers[i - 1]
    # watchers[i] : i ~ i+1초 동안 시청한 사람의 수
    answer = 0
    cur_watchers = 0
    for t in range(adv_time_seconds):
        cur_watchers += watchers[t]
    max_watchers = cur_watchers
    for start_time in range(play_time_seconds - adv_time_seconds + 2):
        # start_time ~ start_time + adv_time_seconds
        cur_watchers += watchers[start_time + adv_time_seconds - 1]
        cur_watchers -= watchers[start_time - 1]
        if cur_watchers > max_watchers:
            max_watchers = cur_watchers
            answer = start_time
    return get_time_string(answer)


def get_seconds(time_str):
    hh, mm, ss = time_str.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def get_time_string(seconds):
    hh = seconds // 3600
    mm = (seconds - hh * 3600) // 60
    ss = seconds - hh * 3600 - mm * 60
    hh_mm_ss = [hh, mm, ss]
    hh_mm_ss = ["{:02d}".format(i) for i in hh_mm_ss]
    return ":".join(hh_mm_ss)


if __name__ == "__main__":
    print(solution("02:03:55", "00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                    "01:37:44-02:02:30"]))  # Expect "01:30:59"
    print(solution("99:59:59", "25:00:00",
                   ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59",
                    "11:00:00-31:00:00"]))  # Expect "01:00:00"
    print(solution("50:00:00", "50:00:00",
                   ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))  # Expect "00:00:00"
    print(solution("00:00:10", "00:00:05",
                   ["00:00:08-00:00:10", "00:00:06-00:00:10"]))  # Expect "00:00:05"
