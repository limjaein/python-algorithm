from collections import deque
import heapq


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]


def findBabyShark():
    for i in range(N):
        for j in range(N):
            if area[i][j] == 9:
                area[i][j] = 0
                return (i, j)



def bfs():
    q = list()
    isVisited = [[False] * N for _ in range(N)]
    size, cnt, time = 2, 0, 0    # 현재 상어 크기, 지금까지 먹은 물고기 수
    result = 0

    sy, sx = findBabyShark()
    heapq.heappush(q, (0, sy, sx))
    isVisited[sy][sx] = True

    while q:
        # 가장 가까우면서 위쪽이며 왼쪽에 있는 위치 물고기 pop
        dist, y, x = heapq.heappop(q)

        if 0 < area[y][x] < size:
            cnt += 1
            area[y][x] = 0
            if cnt == size:
                size += 1
                cnt = 0

            # 물고기 잡아먹을 수 있는 시간 갱신 및 초기화 + 관련 변수 초기화
            result += dist
            dist = 0
            q.clear()
            isVisited = [[False] * N for _ in range(N)]

        # 상하좌우 인접한 한 칸씩 탐색
        for my, mx in zip(dy, dx):
            ny = y + my
            nx = x + mx

            # 인덱스 체크 + 이미 지나간 칸인지 물고기 사이즈가 더 큰지 체크
            if ny < 0 or nx < 0 or ny >= N or nx >= N or isVisited[ny][nx] or area[ny][nx] > size:
                continue

            isVisited[ny][nx] = True
            heapq.heappush(q, (dist + 1, ny, nx))
        dist += 1

    return result


print(bfs())