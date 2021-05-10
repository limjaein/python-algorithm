from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    word_per_length = dict()
    word_per_length_r = dict()

    for word in words:
        if len(word) not in word_per_length:
            word_per_length[len(word)] = list()
            word_per_length_r[len(word)] = list()
        word_per_length[len(word)].append(word)
        word_per_length_r[len(word)].append(word[::-1])

    for length in word_per_length.keys():
        word_per_length[length].sort()
        word_per_length_r[length].sort()

    for query in queries:
        if len(query) not in word_per_length:
            answer.append(0)
            continue

        if query[0] == '?':
            answer.append(count_by_range(word_per_length_r[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))
        else:
            answer.append(count_by_range(word_per_length[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))

    return answer


def count_by_range(words, left, right):
    return bisect_right(words, right) - bisect_left(words, left)


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"]
               , ["fro??", "????o", "fr???", "fro???", "pro?"]))