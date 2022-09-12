# 브루트포스 어림도 없다.. 해설봐버림
# (x1, y1) ~ (x2, y2) 까지에 n만큼의 변화를 주고싶다면
# (x1, y1) = n, (x2 + 1, y1) = -n, (x1, y2+1) = -n, (x2 + 1, y2 + 1) = n


def solution(board, skills):
    answer = 0
    n = len(board)
    m = len(board[0])
    acc_skills = [[0] * m for i in range(n)]

    for skill in skills:
        type, r1, c1, r2, c2, degree = skill

        # 공격이면 음수로 변경
        if type == 1:
            degree = -degree

        # 공격/회복 누적합 계산
        acc_skills[r1][c1] += degree

        if r2 + 1 < n and c2 + 1 < m:
            acc_skills[r2 + 1][c2 + 1] += degree

        if r2 + 1 < n:
            acc_skills[r2 + 1][c1] -= degree

        if c2 + 1 < m:
            acc_skills[r1][c2 + 1] -= degree

    # 오른쪽으로 누적합 계산
    for i in range(n):
        sum = 0
        for j in range(m):
            acc_skills[i][j] += sum
            sum = acc_skills[i][j]

    # 아래쪽으로 누적합 계산
    for i in range(m):
        sum = 0
        for j in range(n):
            acc_skills[j][i] += sum
            sum = acc_skills[j][i]

    for i in range(n):
        for j in range(m):
            board[i][j] += acc_skills[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
