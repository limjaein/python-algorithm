import heapq


class Boxer:
    def __init__(self, num, weight, win_rate, win_cnt):
        self.num = num
        self.weight = weight
        self.win_rate = win_rate
        self.win_cnt = win_cnt

    def __lt__(self, other):
        # 우선순위 1 : 승률
        if self.win_rate > other.win_rate:
            return True
        elif self.win_rate == other.win_rate:
            # 우선순위 2 : 자신보다 몸무게가 무거운 복서를 이긴 횟수
            if self.win_cnt > other.win_cnt:
                return True
            elif self.win_cnt == other.win_cnt:
                # 우선순위 3 : 자신의 몸무게
                if self.weight > other.weight:
                    return True
                elif self.weight == other.weight:
                    # 우선순위 3 : 자신의 번호
                    return self.num < other.num
        return False


def getWinCntByWeight(idx, weights, info):
    cnt = 0
    target_weight = weights[idx]

    for idx, weight in enumerate(weights):
        if info[idx] == 'W' and weight > target_weight:
            cnt += 1

    return cnt


def getWinRate(info):
    cnt = 0
    total = 0

    for i in range(len(info)):
        if info[i] != 'N':
            total += 1
        if info[i] == 'W':
            cnt += 1

    if total == 0:
        return 0
    else:
        return cnt / total


def solution(weights, head2head):
    answer = []
    boxers = []
    N = len(weights)

    print(head2head[0])
    print(head2head[1])

    for i in range(N):
        heapq.heappush(boxers, Boxer(i + 1, weights[i], getWinRate(head2head[i]), getWinCntByWeight(i, weights, head2head[i])))

    while boxers:
        boxer = heapq.heappop(boxers)
        answer.append(boxer.num)

    return answer

solution([50,82,75,120]	,["NLWL","WNLL","LWNW","WWLN"]	)