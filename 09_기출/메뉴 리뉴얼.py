from itertools import combinations
import heapq


def solution():
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    answer = []
    courses = dict()
    max_count = [0] * len(course)
    hq = list()


    for order in orders:
        for count in course:
            for comb in list(map(''.join, combinations(order, count))):
                sorted(comb)
                if comb in courses:
                    prev_cnt = courses.get(comb)
                    courses[comb] = prev_cnt + 1
                else:
                    courses[comb] = 1

    for comb in courses:
        if courses[comb] > 1:
            heapq.heappush(hq, (courses[comb], comb))

    while True:
        cnt, comb = heapq.heappop(hq)
        if max_count[len(comb)]

    answer.sort()
    return answer

print(solution())