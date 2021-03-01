from itertools import permutations

def solution():
    op = ["+", "-", "*", "/"]
    operators = ""
    max_result = -1e9
    min_result = 1e9

    N = input()
    number = list(map(int, input().split()))

    for i, cnt in enumerate(list(map(int, input().split()))):
        for _ in range(cnt):
            operators += op[i]

    for op_comb in set(permutations(operators, len(operators))):
        result = calValue(number, op_comb)
        max_result = max(max_result, result)
        min_result = min(min_result, result)

    print(max_result)
    print(min_result)


def calValue(num_list, op_list):
    result = num_list[0]
    for i, op in enumerate(op_list):
        next = num_list[i + 1]
        if op == "+":
            result += next
        elif op == "-":
            result -= next
        elif op == "*":
            result *= next
        elif op == "/":
            if result < 0:
                result = abs(result) // abs(next) * -1
            else:
                result = abs(result) // abs(next)

    return result


solution()