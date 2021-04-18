import sys
from collections import deque


N, L, R = list(map(int, input().split()))
country = [[0] * N for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for i in range(N):
    country[i] = list(map(int, sys.stdin.readline().split()))

def solution():
    result = 0  # 인구 이동 발생 카운트 저장
    isMoved = True

    while isMoved:
        # 인구 이동 발생 여부 저장
        isMoved = False
        isVisited = [[False] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if isVisited[i][j] or check(i, j):
                    continue
                if move(i, j, isVisited):
                    isMoved = True

        if isMoved:
            result += 1

    return result


def check(y, x):
    for my, mx in zip(dy, dx):
        ny = y + my
        nx = x + mx
        if 0 <= ny < N and 0 <= nx < N:
            if L <= abs(country[y][x] - country[ny][nx]) <= R:
                return False
    return True


def move(y, x, isVisited):
    sdq = deque()
    moveList = deque()
    sum = country[y][x]
    isMoved = False

    isVisited[y][x] = True
    sdq.append((y, x))
    moveList.append((y, x))
    while sdq:
        y, x = sdq.popleft()
        for my, mx in zip(dy, dx):
            ny = y + my
            nx = x + mx

            if ny < 0 or ny >= N or nx < 0 or nx >= N or isVisited[ny][nx]:
                continue

            diff = abs(country[y][x] - country[ny][nx])
            if diff < L or diff > R:
                continue

            isVisited[ny][nx] = True
            sdq.append((ny, nx))
            moveList.append((ny, nx))
            sum += country[ny][nx]

    if len(moveList) > 1:
        isMoved = True

    sum = int(sum/len(moveList))
    for ny, nx in moveList:
        country[ny][nx] = sum

    return isMoved

print(solution())