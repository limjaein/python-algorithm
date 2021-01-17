def solution(str):
    num = int(str[0])
    next = 0

    for i in range(1, len(str)):
        next = int(str[i])
        if num == 0 or num == 1 or next == 0 or next == 1:
            num += next
        else:
            num *= next

    return num


print(solution("567"))


