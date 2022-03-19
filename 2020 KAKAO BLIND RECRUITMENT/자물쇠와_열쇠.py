def rotate(key):
    return list(zip(*reversed(key)))


def initializeOverlap(lock, M, N, L):
    overlap = [[0 for _ in range(L)] for _ in range(L)]
    for x in range(N):
        for y in range(N):
            overlap[x + M - 1][y + M - 1] = lock[x][y]
    return overlap


def checkOpen(overlap, M, N):
    for x in range(N):
        for y in range(N):
            if overlap[x + M - 1][y + M - 1] == 0 or \
                    overlap[x + M - 1][y + M - 1] > 1:
                return False
    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)
    L = N + 2 * M - 1
    for i in range(4):
        key = rotate(key)
        for x in range(M + N):
            for y in range(M + N):
                overlap = initializeOverlap(lock, M, N, L)
                for keyX in range(M):
                    for keyY in range(M):
                        overlap[x + keyX][y + keyY] += key[keyX][keyY]
                if checkOpen(overlap, M, N):
                    return True

    return False


if __name__ == "__main__":
    actual = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
    expected = True
    assert actual == expected
