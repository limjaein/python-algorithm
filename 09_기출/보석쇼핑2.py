# 10
from collections import deque


def solution(gems):
    jewel_cnt = len(set(gems))
    answer = []

    start, end = 0, 0
    gem_cnt = {}

    while end < len(gems):
        gem = gems[end]
        if gem in gem_cnt:
            gem_cnt[gem] += 1
        else:
            gem_cnt[gem] = 1
        while start < end:
            gem = gems[start]
            if gem_cnt[gem] > 1:
                gem_cnt[gem] -= 1
                start += 1
            else:
                break
        if len(gem_cnt) == jewel_cnt:
            answer.append((start + 1, end + 1))
        end += 1


    return sorted(answer, key=lambda x: x[1] - x[0])[0]

print(solution(["AA", "AB", "AC", "AA", "AC"]))
#print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
#print(solution(["XYZ", "XYZ", "XYZ"]))