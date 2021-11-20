import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, c):
        self.character = c
        self.num_words = 0
        self.next_words = dict()

    def insert(self, word):
        self.num_words += 1
        if not word:
            return
        if not word[0] in self.next_words:
            self.next_words[word[0]] = Node(word[0])
        self.next_words[word[0]].insert(word[1:])


def solution(words):
    root = Node('*')
    for word in words:
        root.insert(word)
    answer = 0

    for word in words:
        current = root
        for c in word:
            answer += 1
            child_node = current.next_words[c]
            if child_node.num_words == 1:
                break
            current = child_node
    return answer


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution(["go", "gone", "guild"])
    ans = 7
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution(["abc", "def", "ghi", "jklm"])
    ans = 4
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 3 ------------------")
    sol = solution(["word", "war", "warrior", "world"])
    ans = 15
    assert ans == sol, f"Expected {ans} Actual {sol}"
