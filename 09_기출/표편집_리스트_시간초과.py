# 11:43
from collections import deque
import bisect


def insertNumByIdx(idx, num, table):
    result = []
    result = table[:idx]
    result.append(num)
    result += table[idx:]

    return result


def solution(n, k, cmd):
    answer = ['X'] * n
    table = []
    delete_row_tmp = deque()     # 삭제된 행 번호 저장 deque

    # 행번호를 value로 갖는 리스트 생성
    for i in range(n):
        table.append(i)

    for c in cmd:
        if len(c) == 1:
            if c == "C":        # 삭제
                delete_row_tmp.append(table[k])
                l = k
                r = k - len(table)
                if abs(l) > abs(r):
                    del table[r]
                else:
                    del table[l]
                if k == len(table):
                    k -= 1
            elif c == "Z":      # 삭제 행 복구
                num = delete_row_tmp.pop()
                idx = bisect.bisect_left(table, num)
                table = insertNumByIdx(idx, num, table)
                if k >= idx:
                    k += 1
        else:
            act, move = c.split()
            if act == "U":      # 위로 행 이동
                k -= int(move)
            elif act == "D":    # 아래로 행 이동
                k += int(move)

    for num in table:
        answer[num] = 'O'

    return "".join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))