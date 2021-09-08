# 10
from collections import deque


def solution(gems):
    jewel_cnt = len(set(gems))
    answer = [0, 1e9]
    sub_gems = deque(gems[:jewel_cnt])

    start, end = 0, jewel_cnt - 1

    while True:

        # 만약 보석이 모두 1개 이상일 때
        if jewel_cnt == len(set(sub_gems)):
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            start += 1
            sub_gems.popleft()
        else:
            # 지금 최소 길이보다 크면 뒤만 볼 것
            if end - start >= answer[1] - answer[0]:
                start += 1
                sub_gems.popleft()
                continue

            end += 1
            if end == len(gems):
                break
            else:
                sub_gems.append(gems[end])

    return answer[0] + 1, answer[1] + 1