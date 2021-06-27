import heapq


# 메모리 초과 / 터널 N*(N-1)/2 개 -> 3(N-1) 개
N = int(input())
turnels = list()    # N * N * (N - 1) / 2 = 100,000 * 100,000 * 100,000 / 2 = 100MB * 100MB * 50MB = 500,000KB = 500MB
parents = list()    # 4 * 100,000 = 400,000B
result = 1e9

def init():
    # 행성 정보 입력
    x = list()
    y = list()
    z = list()
    for i in range(N):
        ix, iy, iz = list(map(int, input().split()))
        x.append((ix, i))
        y.append((iy, i))
        z.append((iz, i))


    # 행성 간 거리 저장
    x.sort()
    for i in range(N - 1):
        turnels.append((abs(x[i + 1][0] - x[i][0]), x[i][1], x[i + 1][1]))

    y.sort()
    for i in range(N - 1):
        turnels.append((abs(y[i + 1][0] - y[i][0]), y[i][1], y[i + 1][1]))

    z.sort()
    for i in range(N - 1):
        turnels.append((abs(z[i + 1][0] - z[i][0]), z[i][1], z[i + 1][1]))

    turnels.sort()


def find(idx):
    if parents[idx] == idx:
        return idx
    else:
        # 루트 노드를 경로의 모든 노드 parent로 저장
        parents[idx] = find(parents[idx])
        return parents[idx]


def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA == rootB:
        return False

    # 작은값이 루트노드로 오게함
    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB

    return True


def kruskal(turnels):
    dist_sum = 0
    cnt = 0

    # parent 노드를 자신으로 초기화
    for i in range(N):
        parents.append(i)

    # 전체 터널 조회
    for turnel in turnels:
        dist = turnel[0]
        a = turnel[1]
        b = turnel[2]

        if union(a, b):
            dist_sum += dist
            cnt += 1

        if cnt == N - 1:
            return dist_sum


init()
print(kruskal(turnels))