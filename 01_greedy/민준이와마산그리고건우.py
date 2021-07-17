import heapq

V, E, P = list(map(int, input().split()))
adj = [[] for _ in range(V + 1)]


def solution():
    for _ in range(E):
        a, b, c = list(map(int, input().split()))

        # 인접리스트 생성
        adj[a].append((b, c))
        adj[b].append((a, c))

    # 전체 최단거리가 P를 거쳐가는 최단거리와 같다면 건우 구하기 가능
    if dijkstra(1, V) == dijkstra(1, P) + dijkstra(P, V):
        return "SAVE HIM"
    else:
        return "GOOD BYE"


def dijkstra(s, e):
    newDist = [1e9] * (V + 1)
    q = list()

    newDist[s] = 0
    heapq.heappush(q, (0, s))   # (거리, 노드) 저장

    while q:
        # 가장 최단거리가 짧은 노드 pop
        dist, now = heapq.heappop(q)

        # 이미 처리된 적 있는 노드면 무시
        if newDist[now] < dist:
            continue

        for next, cost in adj[now]:
            # 현재노드를 거쳐가는 거리가 더 짧은 경우 갱신
            if newDist[next] > dist + cost:
                newDist[next] = dist + cost
                heapq.heappush(q, (newDist[next], next))
            
    return newDist[e]

print(solution())
