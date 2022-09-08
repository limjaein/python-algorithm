import math


def convert(n, k):
    convertStr = "0123456789"
    answer = ""

    if n < k:
        return convertStr[n]

    while n >= k:
        n, r = divmod(n, k)
        answer += convertStr[r]
    answer += convertStr[n]

    return answer[::-1]


def isPrimeNumber(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0

    # k 진수로 변환
    converted_n = convert(n, k)

    # 숫자 0으로 split
    for sub_n in converted_n.split('0'):
        # split 된 P를 10진법으로 보았을 때 소수인지 체크
        if sub_n != "" and isPrimeNumber(int(sub_n)):
            answer += 1

    return answer