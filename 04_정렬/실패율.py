from collections import Counter


def solution(N, stages):
    answer = []
    tmp_list = []

    counts = Counter(stages)
    total = len(stages)

    for i in range(1, N+1):
        if total == 0:
            tmp_list.append((0, i))
            continue
        tmp_list.append((counts[i]/total, i))
        total -= counts[i]

    tmp_list = sorted(tmp_list, key=lambda x:(-x[0], x[1]))

    for fail, idx in tmp_list:
        answer.append(idx)

    return answer

print(solution(3, [1, 1, 1, 1, 1]))