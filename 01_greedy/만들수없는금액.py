import itertools


def solution():
    num = 1
    coins = list(map(int, "1 2 3 1 9".split(" ")))
    coins.sort()

    for coin in coins:
        if num < coin:
            break
        num += coin

    print(num)


solution()
