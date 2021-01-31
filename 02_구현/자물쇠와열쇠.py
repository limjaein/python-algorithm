N = 0
M = 0

def solution(key, lock):
    global N, M
    N = len(key)
    M = len(lock)
    keyCnt = count(key, N, 1)
    lockCnt = count(lock, M, 0)

    if lockCnt == 0:
        return True
    elif keyCnt == 0 or keyCnt < lockCnt:
        return False

    # key - lock 겹쳐졌을 때 최대 크기만큼 반복
    for r in range(-N + 1, M):
        for c in range(-N + 1, M):
            if match(key, lock, r, c, lockCnt):
                return True
    return False

# key의 돌기, lock의 홈 카운트 함수
def count(arr, size, num):
    cnt = 0
    for i in range(size):
        for j in range(size):
            if arr[i][j] == num:
                cnt += 1
    return cnt

# key 90도씩 회전하며 자물쇠에 맞춰보는 함수
def match(key, lock, r, c, lockCnt):
    for d in range(4):
        isBlocked = False
        cnt = 0
        if d != 0:
            key = rotate(key)
        for i in range(N):
            for j in range(N):
                if 0 <= r + i < M and 0 <= c + j < M:
                    if key[i][j] == lock[r+i][c+j]:
                        isBlocked = True
                        break
                    elif key[i][j] == 1 and lock[r+i][c+j] == 0:
                        cnt += 1
            if isBlocked:
                break
        if cnt == lockCnt:
            return True
    return False

# key 시계방향으로 90도 회전하는 함수
def rotate(key):
    rotatedKey = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotatedKey[j][N - 1 - i] = key[i][j]
    return rotatedKey