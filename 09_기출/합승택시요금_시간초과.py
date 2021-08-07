# 플로이드 최대 O(n^3) = 200*200*200 = 8,000,000

def solution(n, s, a, b, fares):
    answer = 0
    min_fares = [[1e9] * (n + 1) for _ in range(n + 1)]

    for idx in range(1, n + 1):
        min_fares[idx][idx] = 0

    for fare_info in fares:
        v1, v2, fare = fare_info
        min_fares[v1][v2] = min_fares[v2][v1] = fare

    for stop in range(1, n + 1):
        for v1 in range(1, n + 1):
            for v2 in range(1, n + 1):
                min_fares[v1][v2] = min_fares[v2][v1] = min(min_fares[v1][v2], min_fares[v1][stop] + min_fares[stop][v2])

    # 각자 가는 경우
    answer = min_fares[s][a] + min_fares[s][b]

    # stop 까지 같이 타고가는 경우
    for stop in range(1, n + 1):
        answer = min(answer, min_fares[s][stop] + min_fares[stop][a] + min_fares[stop][b])

    return answer