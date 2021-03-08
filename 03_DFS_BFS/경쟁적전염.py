# (x, y) : x 행 y 열

import sys
from collections import deque

def solution():
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    N, K = map(int, input().split())
    examiner = [[0] * N for _ in range(N)]
    s_list = list()
    dq = deque()

    for i in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            examiner[i][j] = row[j]
            if examiner[i][j] != 0:
                s_list.append((examiner[i][j], i, j))

    S, X, Y = map(int, input().split())

    s_list.sort(key=lambda t:t[0])
    for s in s_list:
        dq.append(s)

    while S != 0:
        S -= 1
        turn = len(dq)

        for _ in range(turn):
            num, x, y = dq.popleft()
            for i in range(4):
                n_x = x + dx[i]
                n_y = y + dy[i]
                if n_x < 0 or n_y < 0 or n_x >= N or n_y >= N or examiner[n_x][n_y] != 0:
                    continue
                examiner[n_x][n_y] = num
                dq.append((examiner[n_x][n_y], n_x, n_y))

    print(examiner[X - 1][Y - 1])


solution()