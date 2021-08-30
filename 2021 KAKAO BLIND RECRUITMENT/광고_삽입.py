# https://programmers.co.kr/learn/courses/30/lessons/72414?language=python3
def solution(play_time, adv_time, logs):
    answer = ''
    play_time_seconds = get_seconds(play_time)
    adv_time_seconds = get_seconds(adv_time)
    print(play_time_seconds)
    print(adv_time_seconds)
    # 0 <= seconds <= 359999
    return answer


def get_seconds(time_str):
    hh, mm, ss = time_str.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


if __name__ == "__main__":
    print(solution("02:03:55", "00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                    "01:37:44-02:02:30"]))  # Expect "01:30:59"
    print(solution("99:59:59", "25:00:00",
                   ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59",
                    "11:00:00-31:00:00"]))  # Expect "01:00:00"
    print(solution("50:00:00", "50:00:00",
                   ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))  # Expect "00:00:00"
