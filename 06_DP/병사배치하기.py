
def solution():
    N = int(input())
    soldiers = list(map(int, input().split()))
    result = 0

    # dp[i] = 0 ~ i 까지 내림차순을 만족하는 최대 부분 수열 길이
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if soldiers[j] > soldiers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    for i in range(N):
        result = max(result, dp[i])

    print(N - result)

solution()




