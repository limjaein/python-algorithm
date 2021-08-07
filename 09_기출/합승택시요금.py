# 다익스트라 최대 O(N * ElogE) ~= 4,000,000 * log(20,000)
# N = 200, E ~= 20,000
import heapq


def dijkstra(n, s, min_fares):
    li = [1e9] * (n + 1)
    q = []
    isVisited = [False] * (n + 1)

    # 출발 정점 설정
    li[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist, now = heapq.heappop(q)
        isVisited[now] = True

        for next in range(1, n + 1):
            # 자신과 이미 방문한 정점 제외
            if next == now or isVisited[next]:
                continue
            # next를 거쳐가는 거리가 더 짧은 경우 갱신
            if li[next] > dist + min_fares[now][next]:
                li[next] = dist + min_fares[now][next]
                heapq.heappush(q, (li[next], next))

    for v in range(s + 1, n + 1):
        min_fares[s][v] = min_fares[v][s] = min(min_fares[s][v], li[v])


def solution(n, s, a, b, fares):
    answer = 0
    min_fares = [[1e9] * (n + 1) for _ in range(n + 1)]

    for idx in range(1, n + 1):
        min_fares[idx][idx] = 0

    for fare_info in fares:
        v1, v2, fare = fare_info
        min_fares[v1][v2] = min_fares[v2][v1] = fare

    for start in range(1, n + 1):
        dijkstra(n, start, min_fares)

    # 각자 가는 경우
    answer = min_fares[s][a] + min_fares[s][b]

    # stop 까지 같이 타고가는 경우
    for stop in range(1, n + 1):
        answer = min(answer, min_fares[s][stop] + min_fares[stop][a] + min_fares[stop][b])

    return answer