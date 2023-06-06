# 시간초과 4
def getMaxDist(deliveries, pickups, n):
    for i in reversed(range(n)):
        if deliveries[i] != 0 or pickups[i] != 0:
            return i + 1
    return 0
        
        
def solution(cap, n, deliveries, pickups):
    answer = 0
    max_dist = getMaxDist(deliveries, pickups, n)

    while max_dist > 0:
        truck = [cap, 0]
        answer += max_dist * 2
        dist = max_dist

        for i in reversed(range(dist)):
            del_cnt = deliveries[i]
            pickup_cnt = pickups[i]

            # 배달 수량이 있으면
            if del_cnt > 0 and truck[0] > 0:
                if del_cnt <= truck[0]:
                    deliveries[i] -= del_cnt
                    truck[0] -= del_cnt
                else:
                    deliveries[i] -= truck[0]
                    truck[0] = 0

            # 수거 수량이 있으면
            if pickup_cnt > 0:
                rest_cap = cap - truck[1]

                if rest_cap >= pickup_cnt:
                    truck[1] += pickup_cnt
                    pickups[i] = 0
                else:
                    pickups[i] -= rest_cap
                    truck[1] = cap

            # 모두 끝난 집이면 인덱스 - 1
            if deliveries[i] == 0 and pickups[i] == 0:
                max_dist = getMaxDist(deliveries, pickups, max_dist)

            # 배달을 마치고, 수거수량이 가득찬 경우 break
            if truck[0] == 0 and truck[1] == cap:
                break

    return answer
