from itertools import combinations
import copy

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

def moveVirus(area, is_visited, y, x):

    for i in range(4):
        n_y = y + dy[i]
        n_x = x + dx[i]

        if n_y < 0 or n_y >= n or n_x < 0 or n_x >= m or is_visited[n_y][n_x] or area[n_y][n_x] == 1:
            continue
        is_visited[n_y][n_x] = True
        area[n_y][n_x] = 2
        moveVirus(area, is_visited, n_y, n_x)


def countSafeArea(area):
    count = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                count += 1
    return count


def solution():
    zero_list = list()
    wall_list = list()
    max_count = 0

    for i in range(n):
        arr[i] = list(map(int, input().split()))
        for j in range(m):
            if arr[i][j] == 0:
                zero_list.append((i, j))

    wall_list = list(combinations(zero_list, 3))

    for wall in wall_list:
        tmp_list = copy.deepcopy(arr)
        is_visited = [[False] * m for _ in range(n)]

        for y, x in wall:
            tmp_list[y][x] = 1

        for i in range(n):
            for j in range(m):
                if tmp_list[i][j] == 2 and not is_visited[i][j]:
                    is_visited[i][j] = True
                    moveVirus(tmp_list, is_visited, i, j)

        max_count = max(max_count, countSafeArea(tmp_list))

    print(max_count)


solution()