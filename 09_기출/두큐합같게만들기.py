# 리스트 슬라이싱 -> deque 더빠르다 -> 그래도 안됨 -> 인덱스 이용하니 된다
#from collections import deque


def solution(queue1, queue2):
    answer = 0

    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1

    target_sum = (sum(queue1) + sum(queue2)) // 2
    left_sum = sum(queue1)

    i, j, l_q1, l_q2 = 0, 0, len(queue1), len(queue2)
    while i < l_q1 + l_q2 and j < l_q2:
        if left_sum < target_sum:
            left_sum += queue2[j]
            queue1.append(queue2[j])
            j += 1
        elif left_sum > target_sum:
            left_sum -= queue1[i]
            i += 1
        else:
            return i + j

    return -1
