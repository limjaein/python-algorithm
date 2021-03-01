import sys
from collections import deque

def solution():
    n, m, k, x = map(int, sys.stdin.readline().split())
    road_list = [[] for _ in range(n+1)]
    min_dist = [-1 for _ in range(n+1)]
    result = list()
    dq = deque()

    for _ in range(m):
        s, e = map(int, sys.stdin.readline().split())
        road_list[s].append(e)

    # 시작 위치를 큐에 넣기
    dq.append((x, 0))
    min_dist[x] = 0
    while dq:
        city, dist = dq.popleft()
        for next in road_list[city]:
            if min_dist[next] == -1:
                dq.append((next, dist + 1))
                min_dist[next] = dist + 1  # 방문 여부 저장

    for idx, dist in enumerate(min_dist):
        if dist == k:
            result.append(idx)

    sorted(result)
    for city in result:
        print(city)

    if len(result) == 0:
        print(-1)


solution()