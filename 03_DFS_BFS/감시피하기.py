import sys
from itertools import combinations

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

xPos = list()
teachers = list()
N = int(input())

map = [['X'] * N for _ in range(N)]

for i in range(N):
    map[i] = list(sys.stdin.readline().split())
    for j in range(N):
        if map[i][j] == 'T':
            teachers.append((i, j))
        elif map[i][j] == 'X':
            xPos.append((i, j))


def findStudents(blocks):
    for idx, teacher in enumerate(teachers):  # 각 선생님 탐색 시작
        y, x = teacher
        for d in range(4):  # 상,하,좌,우 탐색
            ny = y
            nx = x
            while True:
                ny += dy[d]
                nx += dx[d]
                if ny < 0 or ny >= N or nx < 0 or nx >= N or (ny, nx) in blocks:  # 범위 벗어나거나, 장애물 발견 시 탐색 중지
                    break
                if map[ny][nx] == 'S':  # 학생 발견 시 True 리턴
                    return True
    return False  # 모든 선생님 탐색 후 학생 발견 실패 시 False 리턴


def solution():
    # 장애물 조합 반복문
    for comb in list(combinations(xPos, 3)):
        if not findStudents(comb):  # 학생을 찾지 못하는 조합이 있을 경우 YES 출력 후 리턴
            print("YES")
            return
    print("NO")


solution()