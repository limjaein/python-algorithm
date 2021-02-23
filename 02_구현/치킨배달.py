from itertools import combinations


def solution():
    N, M = map(int, input().split())
    min_dist = 1e9

    store_list = list()
    home_list = list()
    tmp = list()
    comb_list = list()

    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] == 1:
                home_list.append((i, j))
            elif tmp[j] == 2:
                store_list.append((i, j))

    for comb_list in list(combinations(store_list, M)):
        dist = 0
        for home in home_list:
            add_dist = 1e9
            for comb in comb_list:
                add_dist = min(add_dist, abs(comb[0]-home[0]) + abs(comb[1]-home[1]))
            dist += add_dist
        min_dist = min(min_dist, dist)

    return min_dist

print(solution())