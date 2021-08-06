from itertools import combinations
import heapq

MAX_CNT_MENU_IN_COURSE = 10


def solution(orders, course):
    answer = []
    courses = dict()    # 조합 가능한 코스 메뉴
    hq = [[] for _ in range(MAX_CNT_MENU_IN_COURSE + 1)]

    for order in orders:
        for menu_cnt in course:
            for comb in list(map(''.join, combinations(sorted(order), menu_cnt))):
                if comb in courses:
                    prev_cnt = courses.get(comb)
                    courses[comb] = prev_cnt + 1
                else:
                    courses[comb] = 1

    for comb in courses:
        # 메뉴 개수 당 주문량이 많은 순으로 정렬
        if courses[comb] > 1:
            heapq.heappush(hq[len(comb)], (-courses[comb], comb))

    for menu_cnt in course:
        prev_cnt = -1
        while hq[menu_cnt]:
            order_cnt, comb = heapq.heappop(hq[menu_cnt])
            order_cnt = -order_cnt

            if prev_cnt == -1 or prev_cnt == order_cnt:
                answer.append(comb)
            else:
                break
            prev_cnt = order_cnt

    answer.sort()
    return answer