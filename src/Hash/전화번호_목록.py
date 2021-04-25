# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phoneBook):
    phoneBook.sort(key=lambda x: len(x))
    trie = [dict(), False]
    for phoneNum in phoneBook:
        current = trie
        for i, c in enumerate(phoneNum):
            if c not in current[0]:
                current[0][c] = [dict(), False]
            if current[1]:
                return False
            current = current[0][c]
            if i == len(phoneNum) - 1:
                current[1] = True

    return True


print(solution(["119", "97674223", "1195524421"]))  # Expect False
print(solution(["123", "456", "789"]))  # Expect True
print(solution(["12", "123", "1235", "567", "88"]))  # Expect False
print(solution(["113", "44", "4544"]))  # Expect True
