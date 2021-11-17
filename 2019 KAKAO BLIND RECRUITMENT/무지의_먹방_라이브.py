# https://programmers.co.kr/learn/courses/30/lessons/42891
def solution(food_times, k):
    left = 0
    right = 100_000_000
    final_threshold = 0
    while left <= right:
        mid = (left + right) // 2
        # print("left:", left, " mid:", mid, " right:", right)
        eaten_amount = get_eaten_amount(food_times, mid)
        if eaten_amount > k:
            right = mid - 1
        else:
            final_threshold = max(final_threshold, mid)
            left = mid + 1
    final_eaten_amount = get_eaten_amount(food_times, final_threshold)
    # print("final_threshold:", final_threshold)
    # print("final_eaten_amount:", final_eaten_amount)

    for i, food_time in enumerate(food_times):
        if food_time > final_threshold:
            if k - final_eaten_amount > 0:
                final_eaten_amount += 1
            else:
                return i + 1
    return -1


def get_eaten_amount(food_times, threshold):
    return sum([min(food_time, threshold) for food_time in food_times])


if __name__ == "__main__":
    print(solution([3, 1, 2], 5))  # Expect 1
    print(solution([1, 5, 5, 5, 5, 6, 7], 31))  # Expect 6
    print(solution([7, 8, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2], 35))  # Expect 2
    print(solution([1, 1, 1, 1], 4))  # Expect -1
    print(solution([3, 1, 1, 1, 2, 4, 3], 12))  # Expect 6
    print(solution([4, 3, 5, 6, 2], 7))  # Expect 3
    print(solution([4, 1, 1, 5], 4))  # Expect 1
    print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))  # Expect 3
    print(solution([4, 2, 3, 6, 7, 1, 5, 8], 27))  # Expect 5
