# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    uid_to_nickname = dict()
    for r in record:
        rs = r.split()
        if rs[0] in ("Enter", "Change"):
            uid_to_nickname[rs[1]] = rs[2]
    enter_message = "님이 들어왔습니다."
    leave_message = "님이 나갔습니다."
    for r in record:
        rs = r.split()
        if rs[0] == "Enter":
            answer.append(uid_to_nickname[rs[1]] + enter_message)
        elif rs[0] == "Leave":
            answer.append(uid_to_nickname[rs[1]] + leave_message)
    return answer


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
    ans = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    assert ans == sol, f"Expected {ans} Actual {sol}"
