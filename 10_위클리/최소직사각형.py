def solution(sizes):
    answer = (0, 0)

    for size in sizes:
        # 명함 가로 세로를 바꾼게 더 작으면 바꿈
        if max(answer[0], size[0]) * max(answer[1], size[1]) > max(answer[0], size[1]) * max(answer[1], size[0]):
            answer = (max(answer[0], size[1]), max(answer[1], size[0]))
        else:
            answer = (max(answer[0], size[0]), max(answer[1], size[1]))

    return answer[0] * answer[1]