# https://programmers.co.kr/learn/courses/30/lessons/60060


import collections


class Node:
    def __init__(self):
        self.next = collections.defaultdict(Node)
        self.count = 0
        self.isWord = False

    def insert(self, word):
        node = self
        node.count += 1
        for w in word:
            node = node.next[w]
            node.count += 1
        node.isWord = True

    def getMatchedCount(self, query):
        node = self
        for i, q in enumerate(query):
            if q == '?':
                return node.count
            if q not in node.next:
                return 0
            node = node.next[q]
        return 0


def solution(words, queries):
    forward_roots = [Node() for _ in range(100_000 + 1)]
    reverse_roots = [Node() for _ in range(100_000 + 1)]
    for word in words:
        forward_roots[len(word)].insert(word)
        reverse_roots[len(word)].insert(word[::-1])
    answer = []
    for query in queries:
        matchedCount = 0
        if query[0] != '?':
            matchedCount += forward_roots[len(query)].getMatchedCount(query)
        else:
            matchedCount += reverse_roots[len(query)].getMatchedCount(query[::-1])
        answer.append(matchedCount)
    return answer


if __name__ == "__main__":
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                   ["fro??", "????o", "fr???", "fro???", "pro?"]))  # Expect [3, 2, 4, 1, 0]
