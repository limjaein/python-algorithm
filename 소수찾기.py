from itertools import permutations

def solution(numbers):
    answer = 0
    lists = []
    isPrime = True

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            lists.append(int(''.join(j)))

    for i in list(set(lists)):
        if i < 2:
            continue

        isPrime = True

        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break

        if isPrime == True:
            answer += 1

    return answer