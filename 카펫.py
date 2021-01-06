import math

def solution(brown, yellow):
    answer = []
    multi = brown + yellow
    row = int(math.sqrt(multi))
    col = 0

    while (1):
        col = multi / row
        if (col == int(col) and row >= col and row * col == multi and (row - 2) * (col - 2) == yellow):
            break
        row += 1

    return [row, col]