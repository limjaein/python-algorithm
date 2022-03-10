# 13:00
from itertools import permutations
import re


operators = ['+', '=', '*']


def solution(expression):
    answer = 0
    op_list = []

    expression = expression.replace("-", "=")

    for op in operators:
        if op in expression:
            op_list.append(op)

    for row in list(permutations(op_list, len(op_list))):
        temp = expression
        for op in row:
            while temp.find(op, 1) != -1:
                temp = calculate(temp, op, temp.find(op, 1))

        answer = max(answer, abs(int(temp)))

    return answer


def calculate(expression, op, idx):
    left_idx = idx
    right_idx = idx
    result = 0

    while left_idx - 1 >= 0:
        left_idx -= 1

        if expression[left_idx] in operators:
            left_idx += 1
            break

        if expression[left_idx] == "-":
            break

    while right_idx + 1 < len(expression):
        right_idx += 1

        if not expression[right_idx] not in operators:
            right_idx -= 1
            break

    left = int(expression[left_idx:idx])
    right = int(expression[idx + 1:right_idx + 1])

    if op == "+":
        result = left + right
    if op == "=":
        result = left - right
    if op == "*":
        result = left * right

    return expression[:left_idx] + str(result) + expression[right_idx + 1:]

solution("100-200*300-500+20")