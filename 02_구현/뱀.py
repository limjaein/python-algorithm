# 보드 0 뱀 1 사과 2
# 상 0 우 1 하 2 좌 3
from collections import deque

dy = []
dx = []

def Solution():
    global dy, dx
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    directions = deque([])
    trace = deque([])

    N = int(input())
    board = [[0] * (N+1) for _ in range(N+1)]
    board[1][1] = 1
    trace.append((1, 1))

    K = int(input())
    for _ in range(K):
        r, c = map(int, input().split())
        board[r][c] = 2

    L = int(input())
    for _ in range(L):
        sec, dir = map(str, input().split())
        directions.append((int(sec), dir))

    r = 1
    c = 1
    time = 1
    dir = 1
    next_time, next_dir = directions.popleft()
    while True:
        # 이동 시작
        n_r = r + dy[dir]
        n_c = c + dx[dir]

        if n_r <= 0 or n_r > N or n_c <= 0 or n_c > N or board[n_r][n_c] == 1: break

        if board[n_r][n_c] == 2: board[n_r][n_c] = 0
        else:
            r, c = trace.popleft()
            board[r][c] = 0
        trace.append((n_r, n_c))
        board[n_r][n_c] = 1
        r, c = n_r, n_c

        # 방향 전환 시기 체크
        if time == next_time:
            if next_dir == 'L': dir = (dir + 3) % 4
            elif next_dir == 'D': dir = (dir + 1) % 4
            if len(directions) > 0: next_time, next_dir = directions.popleft()
            else: next_time = -1
        time += 1

    return time

print(Solution())