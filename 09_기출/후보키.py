from itertools import combinations


def solution(relation):
    answer = 0
    N = len(relation[0])
    student = len(relation)
    candidate_keys = []

    for num in range(1, N + 1):
        for comb_list in combinations(range(0, N), num):
            is_candidate_key = False
            for key in candidate_keys:
                if set(comb_list) >= set(key):
                    is_candidate_key = True
                    break

            if is_candidate_key:
                continue

            temp_values = set()
            for row in relation:
                temp_value = []
                for idx in list(comb_list):
                    temp_value.append(row[idx])
                temp_values.add(tuple(temp_value))

            if len(set(temp_values)) == student:
                candidate_keys.append(comb_list)
                # print(temp_values)
    print(candidate_keys)
    return answer



solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])