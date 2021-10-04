from collections import defaultdict

ROOT = "-"


def solution(enroll, referral, sellers, amounts):
    n = len(enroll)
    answer = defaultdict(int)
    m = len(sellers)
    tree = defaultdict(str)
    for i in range(n):
        tree[enroll[i]] = referral[i]
    for i in range(m):
        update(tree, sellers[i], amounts[i] * 100, answer)
    return [answer[person] for person in enroll]


def update(tree, seller, amount, answer):
    if amount < 1:
        return
    if tree[seller] == [ROOT]:
        answer[seller] += amount
    else:
        ten_percent = int(amount * 0.1)
        answer[seller] += (amount - ten_percent)
        update(tree, tree[seller], ten_percent, answer)


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                   ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])
    ans = [360, 958, 108, 0, 450, 18, 180, 1080]
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                   ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4])
    ans = [0, 110, 378, 180, 270, 450, 0, 0]
    assert ans == sol, f"Expected {ans} Actual {sol}"
