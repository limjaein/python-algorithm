def solution(m, d):
    N = len(m)
    ret = [[0]*N for _ in range(N)]

    if d == 1: # 90도
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d == 2: # 180도
        for r in range(N):
            for c in range(N):
                ret[N-1-r][r] = m[r][c]