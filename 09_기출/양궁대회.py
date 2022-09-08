from itertools import combinations_with_replacement
from collections import Counter


score = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def solution(n, info):
    answer = []
    score_length = len(score)
    counter = Counter()

    sum = 0
    ryan_score = []

    max_sum = 0
    max_score = []

    # n 번의 점수 중복 조합 생성
    for comb in combinations_with_replacement(score, n):
        counter = Counter(comb)

        # 라이언의 점수 카운트 배열 생성
        ryan_score = []
        for i in range(score_length):
            ryan_score.append(counter[10 - i])

        # 점수 로직에 따라 총 점수 차 (라이언 점수 - 어피치 점수) 계산
        sum = 0
        for i in range(score_length):
            if info[i] != 0 and counter[10 - i] != 0:
                if info[i] < counter[10 - i]:
                    sum += (10 - i)
                else:
                    sum += i - 10
            else:
                if info[i] > 0:
                    sum += i - 10
                elif counter[10 - i] > 0:
                    sum += 10 - i

        # 라이언 점수가 더 높은 경우
        if sum > 0:
            # 현재 맥스 점수 차와 같은 경우 낮은 점수를 많이 맞췄을 경우 맥스값 갱신
            if max_sum != 0 and max_sum == sum and int("".join(map(str, max_score))[::-1]) < int("".join(map(str, ryan_score))[::-1]):
                max_sum = sum
                max_score = ryan_score

            if max_sum < sum:
                max_sum = sum
                max_score = ryan_score

    # 라이언이 우승할 방법이 있는 경우
    if max_sum > 0:
        answer = max_score
    else:
        answer = [-1]

    return answer