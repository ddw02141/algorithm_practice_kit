from collections import defaultdict


class Node:
    def __init__(self, idx, x, y):
        self.left = None
        self.right = None
        self.idx = idx
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x

    def __str__(self):
        return "idx: %d left: %d right: %d x: %d y: %d" % (
            self.idx, self.left.idx if self.left else -1, self.right.idx if self.right else -1, self.x, self.y,
        )


def solution(nodeinfo):
    answer = []
    nodeByLevel = {node[1]: list() for node in nodeinfo}
    for i, node in enumerate(nodeinfo):
        nodeByLevel[node[1]].append(Node(i + 1, node[0], node[1]))
    root = nodeByLevel[min(nodeByLevel.keys())][0]
    levels = list(nodeByLevel.keys())
    levels.sort(reverse=True)

    def printNodeByLevel():
        for level in levels:
            print("level:", level)
            for node in nodeByLevel[level]:
                print(node)
        print("------------------------------------")

    for i, level in enumerate(levels):
        nodes = nodeByLevel[level]
        nodes.sort()
        for node in nodes:
            insert(root, node)
        printNodeByLevel()
    return answer


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


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
    ans = [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
    assert ans == sol, f"Expected {ans} Actual {sol}"
