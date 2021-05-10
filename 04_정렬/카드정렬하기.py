import heapq


def solution():
    N = int(input())
    cards = []

    for i in range(N):
        heapq.heappush(cards, int(input()))

    if N == 1:
        return 0

    result = 0
    while cards:
        l = heapq.heappop(cards)
        r = heapq.heappop(cards)
        result += l + r
        if cards:
            heapq.heappush(cards, l + r)

    return result


print(solution())
