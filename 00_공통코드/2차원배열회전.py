def solution(d):
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = len(m)

    ret = [[0] * N for _ in range(N)]

    if d == 1:  # 90도
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d == 2:  # 180도
        for r in range(N):
            for c in range(N):
                ret[N-1-r][N-1-c] = m[r][c]

    return ret


def solution2(d):
    ret = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for _ in range(d):
        ret = list(zip(*ret[::-1]))

    return ret


print(solution(2))
print(solution2(2))
