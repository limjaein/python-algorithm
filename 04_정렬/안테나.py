import sys

def solution():
    N = int(input())
    houses = list(map(int, sys.stdin.readline().split(" ")))
    houses.sort()

    return houses[N//2 - 1 + (N % 2)]

print(solution())