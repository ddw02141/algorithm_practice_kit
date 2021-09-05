# https://programmers.co.kr/learn/courses/30/lessons/72414?language=python3
# Segment Tree https://www.acmicpc.net/blog/view/9
import math


def solution(play_time, adv_time, logs):
    play_time_seconds = get_seconds(play_time)
    adv_time_seconds = get_seconds(adv_time)
    trees = list()
    h = math.ceil(math.log(360_000, 2))
    tree_size = 2 ** (h + 1)
    for log in logs:
        temp_tree = [0 for _ in range(tree_size)]
        start, end = log.split("-")
        start_seconds = get_seconds(start)
        end_seconds = get_seconds(end)
        insert(temp_tree, 0, 0, 360_000, start_seconds, end_seconds)
        trees.append(temp_tree)
    tree = [sum(t) for t in zip(*trees)]
    answer = play_time_seconds - adv_time_seconds
    max_watchers = -1
    for start_time in range(play_time_seconds - adv_time_seconds):
        watchers = query(tree, 0, 0, 360_000, start_time, start_time + adv_time_seconds)
        if watchers > max_watchers:
            max_watchers = watchers
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


def insert(tree, idx, left, right, start, end):
    if left == right:
        if start <= left <= end:
            tree[idx] = 1
        return tree[idx]
    else:
        tree[idx] = insert(tree, idx * 2 + 1, left, (left + right) // 2, start, end) + \
                    insert(tree, idx * 2 + 2, (left + right) // 2 + 1, right, start, end)
        return tree[idx]


def query(tree, idx, left, right, start, end):
    if start > right or end < left:  # left, right, start, end / start, end, left, right
        return 0
    elif start <= left and right <= end:  # start, left, right, end
        return tree[idx]
    left_sum = query(tree, idx * 2 + 1, left, (left + right) // 2, start, end)
    right_sum = query(tree, idx * 2 + 2, (left + right) // 2 + 1, right, start, end)
    return left_sum + right_sum


if __name__ == "__main__":
    print(solution("02:03:55", "00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                    "01:37:44-02:02:30"]))  # Expect "01:30:59"
    print(solution("99:59:59", "25:00:00",
                   ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59",
                    "11:00:00-31:00:00"]))  # Expect "01:00:00"
    print(solution("50:00:00", "50:00:00",
                   ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))  # Expect "00:00:00"
