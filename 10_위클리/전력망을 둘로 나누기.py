def getCount(n, adj, start, disconnted_wire, isVisited, cnt):
    if not isVisited[start]:
        isVisited[start] = True
        cnt += 1

    print(adj[start], cnt)
    for v in adj[start]:
        if v == disconnted_wire:
            continue
        if not isVisited[v]:
            cnt = getCount(n, adj, v, disconnted_wire, isVisited, cnt)
    return cnt


def getDiff(n, adj, disconneted_wire):
    left = getCount(n, adj, disconneted_wire[0], disconneted_wire[1], [False] * (n + 1), 0)
    right = getCount(n, adj, disconneted_wire[1], disconneted_wire[0], [False] * (n + 1), 0)

    return abs(left - right)


def solution(n, wires):
    answer = 1e9
    adj = []

    for _ in range(n + 1):
        adj.append([])

    for wire in wires:
        adj[wire[0]].append(wire[1])
        adj[wire[1]].append(wire[0])

    for wire in wires:
        answer = min(answer, getDiff(n, adj, wire))

    return answer