from collections import deque, Counter

def solution(food_times, k):
    prev = 0
    dq = deque(sorted(food_times))
    counter = Counter(food_times)
    length = len(food_times)

    while dq:
        num = dq.popleft()
        if num == prev:
            continue
        if k - (num - prev) * length >= 0:
            k -= (num - prev) * length
            prev = num
            length -= counter[num]
            if k == 0:
                if length == 0:
                    return -1
                else:
                    break
        else:
            break

    if length == 0:  # 런타임 에러
        return -1

    prev += int(k/length)
    k %= length
    i = 0

    while True:
        if food_times[i] - prev > 0:
            k -= 1
            if k < 0:
                return i + 1
        i = (i + 1) % len(food_times)