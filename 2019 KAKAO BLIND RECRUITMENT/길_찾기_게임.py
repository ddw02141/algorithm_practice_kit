# https://programmers.co.kr/learn/courses/30/lessons/42892
# https://programmers.co.kr/questions/3723
import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, idx, x, y):
        self.left = None
        self.right = None
        self.idx = idx
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.y < other.y


def solution(nodeinfo):
    nodeByLevel = {node[1]: list() for node in nodeinfo}
    for i, node in enumerate(nodeinfo):
        nodeByLevel[node[1]].append(Node(i + 1, node[0], node[1]))
    root = nodeByLevel[max(nodeByLevel.keys())][0]
    levels = list(nodeByLevel.keys())
    levels.sort(reverse=True)

    for i, level in enumerate(levels):
        nodes = nodeByLevel[level]
        nodes.sort()
        for node in nodes:
            insert(root, node)
    preOrderResult = list()
    postOrderResult = list()
    preOrder(root, preOrderResult)
    postOrder(root, postOrderResult)
    return [preOrderResult, postOrderResult]


def insert(current, target):
    if target.x < current.x:
        if not current.left:
            current.left = target
        else:
            insert(current.left, target)
    elif current.x < target.x:
        if not current.right:
            current.right = target
        else:
            insert(current.right, target)


def preOrder(root, answer):
    if not root:
        return
    answer.append(root.idx)
    preOrder(root.left, answer)
    preOrder(root.right, answer)


def postOrder(root, answer):
    if not root:
        return
    postOrder(root.left, answer)
    postOrder(root.right, answer)
    answer.append(root.idx)


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
    ans = [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
    assert ans == sol, f"Expected {ans} Actual {sol}"
