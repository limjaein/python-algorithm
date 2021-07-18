import heapq


M, N = list(map(int, input().split()))
maze = [[0] * M for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

for i in range(N):
    row = input()
    for j, ch in enumerate(row):
        maze[i][j] = int(ch)


def dijkstra():
    q = list()
    # (cost, (y, x)) push
    heapq.heappush(q, (0, (0, 0)))
    result = [[1e9] * M for _ in range(N)]
    result[0][0] = 0

    while q:
        info = heapq.heappop(q)
        cost = info[0]
        y, x = info[1]

        for my, mx in zip(dy, dx):
            ny = y + my
            nx = x + mx

            # 인덱스 체크
            # 무한루프 체크 : 이미 cost 0이거나 현재 최소값보다 크거나 같으면 이동 X
            if ny < 0 or ny >= N or nx < 0 or nx >= M or result[ny][nx] == 0 or result[ny][nx] <= cost + maze[ny][nx]:
                continue

            result[ny][nx] = cost + maze[ny][nx]
            heapq.heappush(q, (result[ny][nx], (ny, nx)))

    return result[N-1][M-1]

print(dijkstra())