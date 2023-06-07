
def solution(cap, n, deliveries, pickups):
    answer = 0
    del_cnt = 0
    pickup_cnt = 0

    for i in range(n-1, -1, -1):
        cnt = 0

        # 배달/수거 수량 차감 -2 -4 /
        del_cnt -= deliveries[i]
        pickup_cnt -= pickups[i]

        # 더 이상 배달 불가할 경우 cap 을 채우고 이동 카운트를 늘림
        while del_cnt < 0 or pickup_cnt < 0:
            del_cnt += cap
            pickup_cnt += cap
            cnt += 1
                
        answer += (i + 1) * 2 * cnt

    return answer
