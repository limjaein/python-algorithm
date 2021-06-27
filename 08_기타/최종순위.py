from collections import deque
import copy

FAIL = "IMPOSSIBLE"
tc = int(input())

def topologySort(n, indegree):
    q = deque()
    result = list()

    # 진입 차수가 0인 팀을 큐에 push
    for i in range(1, n+1):
        if indegree[i] == 0:
          q.append(i)

    for i in range(1, n+1):
        # 큐 사이즈가 0이면 사이클 발생
        if len(q) == 0:
            print(FAIL)
            return

        result.append(q.popleft())
        for j in range(1, n+1):
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)

    print(" ".join(map(str, result)))

def solution():
    n = int(input())    # 팀의 수
    last_ranks = list(map(int, input().split()))    # 작년 순위 순서
    m = int(input())    # 상대 등수가 바뀐 쌍의 수
    indegree = [0] * (n+1)    # 각 팀의 진입차수정보
    new_indegree = list()

    if m == 0:
        print(" ".join(map(str, last_ranks)))
        return

    for idx, team in enumerate(last_ranks):
        indegree[team] = idx;

    new_indegree = copy.deepcopy(indegree)

    for _ in range(m):
        a, b = list(map(int, input().split()))
        # a -> b 로 바뀐 경우


        if indegree[a] > indegree[b]:
            new_indegree[a] -= 1
            new_indegree[b] += 1
        else:
            new_indegree[b] -= 1
            new_indegree[a] += 1

    topologySort(n, new_indegree)

for _ in range(tc):
    solution()