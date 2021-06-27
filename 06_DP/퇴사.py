N = int(input())
dp = [0] * N
T = [0] * N
P = [0] * N
maxProfit = 0

for i in range(N):
    T[i], P[i] = list(map(int, input().split()))

def makePlan(idx, sum):
    global maxProfit
    nextTime = 0

    for i in range(idx, N):
        nextTime = i + T[i]
        if nextTime > N:
            continue
        makePlan(nextTime, sum + P[i])
    maxProfit = max(maxProfit, sum)
    return maxProfit

print(makePlan(0, 0))


import queue

q = queue.Queue

q.put()
q.get()

