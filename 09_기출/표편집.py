def solution(n, k, cmd):
    answer = ['O'] * n
    dlList = [[0] * 2 for _ in range(n)]
    delete_row_tmp = []     # 삭제된 행 번호 저장 stack

    for i in range(len(dlList)):
        dlList[i][0] = i - 1
        dlList[i][1] = i + 1

    for c in cmd:
        if c[0] == "C":        # 삭제
            prev, next = dlList[k]
            delete_row_tmp.append((prev, next, k))
            answer[k] = 'X'

            # 삭제노드가 마지막 노드일 경우
            if next == n:
                k = prev
            else:
                k = next

            if prev == -1:
                # 첫 노드일 경우 next 노드와 삭제노드의 prev 연결
                dlList[next][0] = prev
            elif next == n:
                # 마지막 노드 일 경우 prev 노드와 삭제노드의 next 연결
                dlList[prev][1] = next
            else:
                dlList[prev][1] = next
                dlList[next][0] = prev
        elif c[0] == "Z":      # 삭제 행 복구
            prev, next, d = delete_row_tmp.pop()
            answer[d] = 'O'

            if prev == -1:
                # 첫 노드일 경우 next 노드와 연결
                dlList[next][0] = d
            elif next == n:
                # 마지막 노드 일 경우 prev 노드와 연결
                dlList[prev][1] = d
            else:
                dlList[prev][1] = d
                dlList[next][0] = d
        elif c[0] == "U":      # 위로 행 이동
            for _ in range(int(c[2:])):
                k = dlList[k][0]
        elif c[0] == "D":    # 아래로 행 이동
            for _ in range(int(c[2:])):
                k = dlList[k][1]

    return "".join(answer)