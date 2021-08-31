from itertools import product


def makeComb(alphabets):
    result = []

    for l in range(1, len(alphabets) + 1):
        for comb in list(map(''.join, product(alphabets, repeat=l))):
            result.append(comb)

    return sorted(result)


def solution(word):
    answer = 0
    alphabets = ['A', 'E', 'I', 'O', 'U']

    for idx, comb in enumerate(makeComb(alphabets)):
        print(comb)
        if comb == word:
            return idx + 1


print(solution("EIO"))